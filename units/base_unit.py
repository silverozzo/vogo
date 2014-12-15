from guts.config import Config

class BaseUnit:
	_knit = ''
	
	def __init__(self):
		_line_offset = 0
	
	def set_line_offset(self, offset):
		""""""
		self._line_offset = offset
	
	def get_line_offset(self):
		"""выдача смещения нотного знака"""
		return self._line_offset
	
	def get_stave_offset(self, check=''):
		return Config.draw_center;
	
	def get_unit_width(self):
		"""выдача ширины нотного знака"""
		raise Exception('must be implemented')
	
	def draw(self, stave_image):
		pass
	
	def set_knit(self, knit):
		"""установка, что знак будет находиться в вязке"""
		pass
	
	def set_rod_length(self, length):
		pass