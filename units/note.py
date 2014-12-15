from guts.config import Config
from service.logger import Logger
from units.base_unit import BaseUnit

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


tone_offsets = {
	'c' : 12, 'd' : 10, 'e' : 8, 'f' : 6, 'g' : 4, 'a' : 2, 'b' : 0}


class NoteUnit(BaseUnit):
	add_dur = False
	_octave = 0
	_forced_rod = ''
	_add_rod_length = None
	_ignore_flag = False
	_alterative = ''
	_alter_offset = 0
	_tone_offset = None
	_mark = None
	
	def print_explode(self, level=0):
		lev_offset = "\t" * (level)
		print(lev_offset + "NoteUnit:")
		lev_offset = "\t" * (level + 1)
		print(lev_offset + "tone          : " + self._tone)
		print(lev_offset + "duration      : " + str(self._duration))
		print(lev_offset + "knit          : " + str(self._knit))
		print(lev_offset + "add_rod_length: " + str(self._add_rod_length))
	
	def __init__(self, tone='c', duration=1):
		self.add_dur = False
		self._octave = 0
		self._forced_rod = ''
		self._add_rod_length = None
		self._ignore_flag = False
		self._alterative = ''
		self._alter_offset = 0
		self._tone_offset = None
		self._mark = None
		self._knit = None
		if duration & (duration-1) != 0:
			Logger.log('note: init: wrong duration: ' + str(duration))
			duration = 0
		self._tone = tone
		self._duration = int(duration)
	
	def get_unit_width(self):
		if self._duration == 0:
			return 0 + self._alter_offset
		return 5 + 8 + self._alter_offset
	
	def get_stave_offset(self, check=''):
		if self._tone_offset is None:
			self._make_stave_offset()
		return self._tone_offset
	
	def set_octave(self, octave):
		self._octave = octave
	
	def set_alterative(self, alter):
		self._alterative = alter
		if self._alterative == 'flat':
			self._alter_offset = 4
		if self._alterative == 'bekar':
			self._alter_offset = 4
		if self._alterative == 'sharp':
			self._alter_offset = 6
	
	def set_line_offset(self, offset):
		BaseUnit.set_line_offset(self, offset)
		self._line_offset += self._alter_offset
	
	def set_forced_rod(self, force):
		self._forced_rod = force
	
	def set_ignore_flag(self, ignore):
		self._ignore_flag = ignore
	
	def set_rod_length(self, length):
		self._add_rod_length = length
	
	def set_knit(self, knit):
		self._knit = knit
	
	def get_tone(self):
		return self._tone
	
	def get_duration(self):
		return self._duration
	
	def set_mark(self, mark):
		self._mark = mark
	
	def draw(self, stave_image, force_on_knit = False):
		if not force_on_knit and self._knit is not None :
			return;
		#self.print_explode()
		self._make_stave_offset()
		with Drawing() as draw, Color('black') as color:
			self._draw_add_stave(stave_image, draw)
			draw.stroke_color = color
			self._draw_head(stave_image, draw)
			self._draw_rod(stave_image, draw)
			self._draw_add_dur(stave_image, draw)
			self._draw_alterative(stave_image, draw)
			self._draw_mark(stave_image)
	
	def _draw_add_stave(self, stave_image, draw):
		if self._octave < 0 and self._tone in ('a', 'b'):
			with Color('silver') as color:
				draw.stroke_color = color
				draw.line((self._line_offset - 2, Config.draw_center + 12),
					(self._line_offset + 7, Config.draw_center + 12))
				draw.draw(stave_image)
		if self._octave == 0 and self._tone == 'c':
			with Color('silver') as color:
				draw.stroke_color = color
				draw.line((self._line_offset - 2, Config.draw_center + 12),
					(self._line_offset + 7, Config.draw_center + 12))
				draw.draw(stave_image)
		if self._octave > 0 and self._tone in ('a', 'b'):
			with Color('silver') as color:
				draw.stroke_color = color
				draw.line((self._line_offset - 2, Config.draw_center - 12),
					(self._line_offset + 7, Config.draw_center - 12))
				draw.draw(stave_image)
	
	def _draw_head(self, stave_image, draw):
		if self._duration == 0:
			return;
		back_color = Color('gray20') 
		if self._duration <= 2:
			back_color = Color('transparent')
		draw.fill_color = back_color
		draw.stroke_color = Color('black')
		draw.stroke_width = 0.5
		draw.circle((self._line_offset + 2, self._tone_offset),
			(self._line_offset + 4, self._tone_offset))
		draw.draw(stave_image)
	
	def _draw_rod(self, stave_image, draw):
		if self._duration == 0:
			return;
		rod_dir = self._get_rod_dir()
		if rod_dir == '':
			return
		
		#	рисуем штиль
		if rod_dir == 'up':
			full_height = self._tone_offset - self._get_rod_length()
			draw.line((self._line_offset + 4, self._tone_offset),
				(self._line_offset + 4, full_height))
		if rod_dir == 'down':
			full_height = self._tone_offset + self._get_rod_length()
			draw.line((self._line_offset, self._tone_offset),
				(self._line_offset, full_height))
		draw.draw(stave_image)
		
		#	рисуем флажок
		if self._ignore_flag or self._knit is not None:
			return
		if rod_dir == 'up' and self._duration >= 8:
			fl = 0
			for i in filter(lambda x: 0 == (x & (x-1)), 
					range(8, self._duration + 1)):
				draw.line((self._line_offset + 5, self._tone_offset - 12 + fl),
					(self._line_offset + 7, self._tone_offset - 10 + fl))
				draw.line((self._line_offset + 5, self._tone_offset - 11 + fl),
					(self._line_offset + 7, self._tone_offset - 9 + fl))
				draw.line((self._line_offset + 8, self._tone_offset - 9 + fl),
					(self._line_offset + 7, self._tone_offset - 5 + fl))
				fl += 3
		if rod_dir == 'down' and self._duration >= 8:
			fl = 0
			for i in filter(lambda x: 0 == (x & (x-1)), 
					range(8, self._duration + 1)):
				draw.line((self._line_offset + 1, self._tone_offset + 12 - fl),
					(self._line_offset + 3, self._tone_offset + 10 - fl))
				draw.line((self._line_offset + 1, self._tone_offset + 11 - fl),
					(self._line_offset + 3, self._tone_offset + 9 - fl))
				draw.line((self._line_offset + 4, self._tone_offset + 10 - fl),
					(self._line_offset + 3, self._tone_offset + 4 - fl))
				fl += 3
		draw.draw(stave_image)
	
	def _draw_add_dur(self, stave_image, draw):
		if self._duration == 0:
			return;
		if not self.add_dur:
			return
		add_offset = 0
		if (self._tone in ('c', 'e', 'g', 'b') and self._octave == 0) or \
				(self._tone not in ('c', 'e', 'g', 'b') and self._octave == 1):
			add_offset = -2
		draw.line((self._line_offset + 7, self._tone_offset + add_offset),
			(self._line_offset + 8, self._tone_offset + add_offset))
		draw.draw(stave_image)
	
	def _draw_alterative(self, stave_image, draw):
		if self._alterative == '':
			return
		line_offset = self._line_offset - self._alter_offset
		if self._alterative == 'sharp':
			draw.line((line_offset + 1, self._tone_offset - 4),
				(line_offset + 1, self._tone_offset + 5))
			draw.line((line_offset + 3, self._tone_offset - 5),
				(line_offset + 3, self._tone_offset + 4))
			draw.line((line_offset + 0, self._tone_offset - 1),
				(line_offset + 4, self._tone_offset - 3))
			draw.line((line_offset + 0, self._tone_offset + 3),
				(line_offset + 4, self._tone_offset + 1))
		if self._alterative == 'bekar':
			draw.line((line_offset + 0, self._tone_offset - 6),
				(line_offset + 0, self._tone_offset + 3))
			draw.line((line_offset + 2, self._tone_offset - 3),
				(line_offset + 2, self._tone_offset + 6))
			draw.line((line_offset + 1, self._tone_offset - 2),
				(line_offset + 1, self._tone_offset - 2))
			draw.line((line_offset + 1, self._tone_offset + 2),
				(line_offset + 1, self._tone_offset + 2))
		if self._alterative == 'flat':
			draw.line((line_offset + 0, self._tone_offset - 6),
				(line_offset + 0, self._tone_offset + 2))
			draw.line((line_offset + 1, self._tone_offset - 2),
				(line_offset + 2, self._tone_offset - 1))
			draw.line((line_offset + 2, self._tone_offset + 0),
				(line_offset + 0, self._tone_offset + 2))
		draw.draw(stave_image)
	
	def _make_stave_offset(self):
		self._tone_offset = 0
		if self._tone in tone_offsets:
			self._tone_offset = tone_offsets[self._tone]
		self._tone_offset -= self._octave * 14 - Config.draw_center
	
	def _get_rod_dir(self):
		if self._forced_rod == 'up' or self._knit == 'up':
			return 'up'
		if self._forced_rod == 'down' or self._knit == 'down':
			return 'down'
		if self._octave == -1 and self._duration > 1:
			return 'up'
		if self._duration > 1 and self._octave == 0 and self._tone != 'b':
			return 'up'
		if self._duration > 1 and self._tone == 'b':
			return 'down'
		if self._duration > 1 and self._octave > 0:
			return 'down'
		return ''
	
	def _get_rod_length(self):
		result = 0
		if self._add_rod_length is None:
			result = 14
		if result == 0 and self._knit == 'up':
			result = (12 - self._add_rod_length - Config.draw_center + 
				self._tone_offset)
		if result == 0 and self._knit == 'down':
			result = (12 + self._add_rod_length + Config.draw_center - 
				self._tone_offset)
		return result
	
	def _draw_mark(self, stave_image):
		if self._duration == 0:
			return;
		if self._mark is None:
			return
		mark_file = Config.mark_figure_dir + 'mark_' + self._mark + '.png'
		mark_image = Image(filename=mark_file)
		stave_image.composite(mark_image, self._line_offset, 0)