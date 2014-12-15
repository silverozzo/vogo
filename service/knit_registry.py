from guts.config import Config
from service.logger import Logger

from wand.color import Color
from wand.drawing import Drawing


class Knit:
	start = None
	finish = None
	direction = None
	level = 0
	adds = []
	base = None
	min = None
	max = None
	
	def __init__(self, direction, level):
		self.direction = direction
		self.level = level
		self.start = None
		self.finish = None
		self.adds = []
		self.base = None
		self.min = None
		self.max = None


class KnitRegistry:
	_knits = []
	_knitted = 0
	_prev_unit = None
	
	def __init__(self):
		self._knits = []
		self._knitted = 0
		self._prev_unit = None
	
	def take_letter(self, letter):
		if letter[0] == '[':
			self._knitted += 1
			dir = None
			if '!up' in letter:
				dir = 'up'
			if '!down' in letter:
				dir = 'down'
			knit = Knit(dir, self._knitted - 1)
			self._knits.append(knit)
			if self._knitted > 1:
				for item in reversed(self._knits[:-1]):
					if item.finish is None:
						knit.base = item
						break
			return True
		if letter == ']':
			for item in reversed(self._knits):
				if item.finish is None:
					item.finish = self._prev_unit
					break
			self._knitted -= 1
			return True
		return False
	
	def take_unit(self, unit):
		if self._knitted == 0:
			return False
		for item in reversed(self._knits):
			if item.start is None:
				item.start = unit
			if (item.direction is None and 
					unit.get_stave_offset() >= Config.draw_center):
				item.direction = 'up'
				unit.set_knit('up')
			if (item.direction is None and 
					unit.get_stave_offset() < Config.draw_center):
				item.direction = 'down'
				unit.set_knit('down')
			if item.finish is None:
				item.adds.append(unit)
				if item.min is None or item.min > unit.get_stave_offset():
					item.min = unit.get_stave_offset('min')
				if item.max is None or item.max < unit.get_stave_offset():
					item.max = unit.get_stave_offset('max')
		if self._knits[-1].direction is not None:
			unit.set_knit(self._knits[-1].direction)
		self._prev_unit = unit
		return True
	
	def draw(self, stave_image):
		with Drawing() as draw, Color('black') as color:
			draw.stroke_width = 2.5
			draw.stroke_color = color
			for item in self._knits:
				if item.finish is None:
					Logger.log('knit not finished: ' + 
						str(self._knits.index(item)))
					continue
				
				knit_offset_min = item.min
				knit_offset_max = item.max
				if item.base is not None:
					cur = item.base
					while cur is not None:
						knit_offset_min = cur.min
						knit_offset_max = cur.max
						cur = cur.base
				knit_offset_min -= Config.draw_center + 2
				knit_offset_max -= Config.draw_center - 2
				knit_offset_min = max(-6, knit_offset_min)
				knit_offset_max = min(2, knit_offset_max)
				
				for add_unit in item.adds:
					if item.direction == 'up':
						add_unit.set_rod_length(knit_offset_min)
					if item.direction == 'down':
						add_unit.set_rod_length(knit_offset_max)
					add_unit.draw(stave_image, True)
				
				level = item.level * 4
				below = Config.draw_center + 11 - level + knit_offset_max
				above = Config.draw_center - 11 + level + knit_offset_min
				
				#	здесь у нас ситуация, когда в вязке неполная планка (всего 
				#	одна нота завязана на саму себя)
				if item.start == item.finish:
					prev_knit_start = None
					prev_knit_finish = None
					#	здесь нам нужно найти вышестоящую вязку, чтобы 
					#	определить в какую сторону будет смотреть неполная 
					#	планка
					for prev in reversed(
							self._knits[:self._knits.index(item)]):
						if prev.start == item.start:
							prev_knit_start = prev.start
						if prev.finish == item.finish:
							prev_knit_finish = prev.finish
					
					#	здесь отрисуем наши недовязки
					if (prev_knit_start == item.start and 
							item.direction == 'up'):
						self._draw_thick_line(draw, 
							item.start.get_line_offset() + 4, above, 
							item.start.get_line_offset() + 8, above)
					if (prev_knit_finish == item.finish and 
							item.direction == 'up'):
						self._draw_thick_line(draw, 
							item.finish.get_line_offset(), above, 
							item.finish.get_line_offset() + 4, above)
					if (prev_knit_start == item.start and 
							item.direction == 'down'):
						self._draw_thick_line(draw, 
							item.start.get_line_offset(), below, 
							item.start.get_line_offset() + 4, below)
					if (prev_knit_finish == item.finish and 
							item.direction == 'down'):
						self._draw_thick_line(draw, 
							item.start.get_line_offset() - 4, below, 
							item.start.get_line_offset(), below)
				
				if item.start != item.finish and item.direction == 'up':
					self._draw_thick_line(draw, 
						item.start.get_line_offset() + 4, above, 
						item.finish.get_line_offset() + 4, above)
				if item.start != item.finish and item.direction == 'down':
					self._draw_thick_line(draw, 
						item.start.get_line_offset(), below, 
						item.finish.get_line_offset(), below)
				draw.draw(stave_image)
	
	def _draw_thick_line(self, draw, start_x, start_y, finish_x, finish_y):
		draw.line((int(start_x), int(start_y)), (int(finish_x), int(finish_y)))
