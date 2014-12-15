from guts.config import Config
from service.knit_registry import KnitRegistry
from service.liga_registry import LigaRegistry
from service.logger import Logger
from service.trip_registry import TripRegistry
from service.unit_factory import UnitFactory

from wand.color import Color
from wand.display import display
from wand.drawing import Drawing
from wand.image import Image


unit_factory = UnitFactory()

class LineMaker:
	def process(line):
		queue = filter(lambda x: False if x == '' else True, line.split(' '))
		
		units = []
		line_offset = 0
		knits = KnitRegistry()
		ligas = LigaRegistry()
		trips = TripRegistry()
		
		for letter in queue:
			if knits.take_letter(letter): continue
			if ligas.take_letter(letter): continue
			if trips.take_letter(letter): continue
			
			unit = unit_factory.get(letter)
			if unit is None: continue
			
			unit.set_line_offset(line_offset)
			line_offset += unit.get_unit_width()
			units.append(unit)
			
			knits.take_unit(unit)
			ligas.take_unit(unit)
			trips.take_unit(unit)
		
		if line_offset == 0:
			return None
		
		height = Config.draw_center*2 + 1
		image = Image(width=line_offset, height=height, 
			background=Color('white'))
		LineMaker.draw_stave(image);
		for unit in units:
			unit.draw(image)
		knits.draw(image)
		ligas.draw(image)
		trips.draw(image)
		return image
	
	def draw_stave(image):
		with Drawing() as draw, Color('silver') as color:
			draw.stroke_color = color
			draw.line((0, Config.draw_center), 
				(image.width, Config.draw_center))
			draw.line((0, Config.draw_center - 4), 
				(image.width, Config.draw_center - 4))
			draw.line((0, Config.draw_center - 8), 
				(image.width, Config.draw_center - 8))
			draw.line((0, Config.draw_center + 4), 
				(image.width, Config.draw_center + 4))
			draw.line((0, Config.draw_center + 8), 
				(image.width, Config.draw_center + 8))
			draw(image)