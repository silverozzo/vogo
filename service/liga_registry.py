from guts.config import Config
from service.logger import Logger

from wand.color import Color
from wand.drawing import Drawing


class Liga:
	start = None
	finish = None
	direction = None
	
	def print_explode(self, level=0):
		lev_offset = "\t" * level
		print(lev_offset + "Liga:")
		lev_offset = "\t" * (level + 1)
		if self.direction is None:
			print(lev_offset + "direction: None")
		else:
			print(lev_offset + "direction: " + self.direction)
		if self.start is None:
			print(lev_offset + "start    : None")
		else:
			print(lev_offset + "start    :")
			self.start.print_explode(level + 2)
		if self.finish is None:
			print(lev_offset + "finish   : None")
		else:
			print(lev_offset + "finish   :")
			self.finish.print_explode(level + 2)
	
	def __init__(self, direction):
		self.direction = direction


class LigaRegistry:
	_ligas = []
	_ligated = False
	_prev_unit = None
	
	def __init__(self):
		self._ligas = []
		self._ligated = False
		self._prev_unit = None
	
	def take_letter(self, letter):
		if letter[0] == '(':
			dir = 'up' if '!up' in letter else (
				'down' if '!down' in letter else None)
			self._ligated = True
			self._ligas.append(Liga(dir))
			return True
		if letter[0] == ')':
			if len(letter) > 1 and letter[1].isnumeric():
				self._ligas[int(letter[1])].finish = self._prev_unit
			else:
				for liga in reversed(self._ligas):
					if liga.finish is None:
						liga.finish = self._prev_unit
						break
			self._ligated = False
			for liga in reversed(self._ligas):
				if liga.finish is None:
					self._ligated = True
			return True
		return False
	
	def take_unit(self, unit):
		if not self._ligated:
			return False
		for item in reversed(self._ligas):
			item.start = unit if item.start is None else item.start
		self._prev_unit = unit
		return True
	
	def draw(self, stave_image):
		for item in self._ligas:
			
			#item.print_explode()
			
			if item.finish is None:
				Logger.log("liga is not finished: " + 
					str(self._ligas.index(item)))
				continue
			
			if item.direction is None:
				if item.start.get_stave_offset() > Config.draw_center:
					item.direction = 'down'
				if item.start.get_stave_offset() < Config.draw_center:
					item.direction = 'up'
				if item.start.get_stave_offset() == Config.draw_center:
					if item.finish.get_stave_offset() > Config.draw_center:
						item.direction = 'down'
					if item.finish.get_stave_offset() < Config.draw_center:
						item.direction = 'up'
					if item.finish.get_stave_offset() == Config.draw_center:
						item.direction = 'up'
			
			(p0_x, p0_y, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y) = [0] * 8
			p0_x = item.start.get_line_offset() + 4
			p3_x = item.finish.get_line_offset() - 1
			p1_x = p0_x + (p3_x-p0_x) / 3
			p2_x = p3_x - (p3_x-p0_x) / 3
			
			if item.direction == 'down':
				p0_y = item.start.get_stave_offset() + 5
				p3_y = item.finish.get_stave_offset() + 5
				p1_y = p0_y + (p3_y-p0_y) / 3 + (p3_x-p0_x) / 3
				p2_y = p3_y - (p3_y-p0_y) / 3 + (p3_x-p0_x) / 3
			if item.direction == 'up':
				p0_y = item.start.get_stave_offset() - 4
				p3_y = item.finish.get_stave_offset() - 4
				p1_y = p0_y + (p3_y-p0_y) / 3 - (p3_x-p0_x) / 3
				p2_y = p3_y - (p3_y-p0_y) / 3 - (p3_x-p0_x) / 3
			
			with Drawing() as draw:
				draw.fill_color = Color('transparent')
				draw.stroke_color = Color('black')
				draw.bezier(((p0_x, p0_y), (p1_x, p1_y), (p2_x, p2_y), 
					(p3_x, p3_y)))
				draw.draw(stave_image)
