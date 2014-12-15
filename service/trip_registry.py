from guts.config import Config
from service.logger import Logger

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


class Trip:
	def __init__(self):
		self.start = None
		self.final = None
		pass
	
	def print_explode(self, level=0):
		lev_offset = "\t" * level
		print(lev_offset + "Trip:")
		lev_offset = "\t" * (level + 1)
		if self.start is None:
			print(lev_offset + "start: None")
		else:
			print(lev_offset + "start:")
			self.start.print_explode(level + 2)
		if self.final is None:
			print(lev_offset + "final: None")
		else:
			print(lev_offset + "final:")
			self.final.print_explode(level + 2)

class TripRegistry:
	def __init__(self):
		self._triplets = []
		self._tripleted = 0
	
	def take_letter(self, letter):
		if letter == '333':
			self._triplets.append(Trip())
			self._tripleted = 3
			return True
		return False
	
	def take_unit(self, unit):
		if self._tripleted == 3:
			self._triplets[-1].start = unit
			self._tripleted -= 1
			return True
		if self._tripleted == 2:
			self._tripleted -= 1
			return True
		if self._tripleted == 1:
			self._triplets[-1].final = unit
			self._tripleted -= 1
			return True
		return False
	
	def draw(self, stave_image):
		for trip in self._triplets:
			#trip.print_explode()
			
			if trip.start is None or trip.final is None:
				Logger.log('triplet not complete')
				continue
			
			with Drawing() as draw, Color('black') as color:
				draw.stroke_width = 1
				draw.stroke_color = color
				draw.line((trip.start.get_line_offset() + 0, 
					Config.draw_center - 18), 
					(trip.final.get_line_offset() + 5, 
					Config.draw_center - 18))
				draw.line((trip.start.get_line_offset() + 0, 
					Config.draw_center - 18), 
					(trip.start.get_line_offset() + 0, 
					Config.draw_center - 14))
				draw.line((trip.final.get_line_offset() + 5, 
					Config.draw_center - 18), 
					(trip.final.get_line_offset() + 5, 
					Config.draw_center - 14))
				draw.draw(stave_image)
				
				trip_file = Config.static_unit_dir + 'figure_3.png'
				trip_mark = Image(filename=trip_file)
				stave_image.composite(trip_mark, 
					trip.start.get_line_offset() + 6, Config.draw_center - 26)