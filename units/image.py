from guts.config import Config
from units.base_unit import BaseUnit

from wand.image import Image


class ImageUnit(BaseUnit):
	def __init__(self, file, width):
		self._file = file
		self._width = width
	
	def print_explode(self, level=0):
		lev_offset = "\t" * (level)
		print(lev_offset + "ImageUnit:")
		lev_offset = "\t" * (level+1)
		print(lev_offset + "file : " + self._file)
		print(lev_offset + "width: " + str(self._width))
	
	def get_unit_width(self):
		return self._width
	
	def draw(self, stave_image):
		with Image(filename=self._file) as unit_image:
			stave_offset = int(Config.draw_center - (unit_image.height-1) / 2)
			stave_image.composite(unit_image, self._line_offset, stave_offset)