from guts.config import Config
from units.base_unit import BaseUnit

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


class TactUnit(BaseUnit):
	_upper = None
	_lower = None
	
	def __init__(self, upper, lower):
		self._upper = upper
		self._lower = lower
	
	def print_explode(self, level=0):
		lev_offset = "\t" * (level)
		print(lev_offset + "TactUnit:")
		lev_offset = "\t" * (level+1)
		print(lev_offset + "upper: " + self._upper)
		print(lev_offset + "lower: " + self._lower)
	
	def get_unit_width(self):
		return 11
	
	def draw(self, stave_image):
		with Drawing() as draw, Color('black') as color:
			draw.stroke_color = color
			draw.line((self._line_offset, Config.draw_center), 
				(self._line_offset + 6, Config.draw_center))
			draw.draw(stave_image)
			upper = Config.static_unit_dir + "figure_" + self._upper + ".png"
			lower = Config.static_unit_dir + "figure_" + self._lower + ".png"
			upper_image = Image(filename=upper)
			lower_image = Image(filename=lower)
			stave_image.composite(upper_image, 
				self._line_offset + 1, Config.draw_center - 8)
			stave_image.composite(lower_image, 
				self._line_offset + 1, Config.draw_center + 2)