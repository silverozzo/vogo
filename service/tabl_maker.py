from guts.config import Config
from service.line_maker import LineMaker
from service.logger import Logger

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


class TablMaker:
	def process(lines, name, out_file):
		#	здесь кусок про соединение строк в одну, если последний символ '/'
		imploded = []
		curline = ''
		for line in lines:
			curline += line
			if len(curline) > 0 and curline[-1] != '/':
				imploded.append(curline)
				curline = ''
			else:
				curline = curline[:-1]
		imploded.append(curline)
		lines = imploded
		
		#	здесь каждая строка кода превращается в картинку
		staves = []
		for line in lines:
			stave_line = LineMaker.process(line)
			if stave_line is not None:
				staves.append(stave_line)
		
		#	здесь готовим основу, в которую будем все размещать
		max_width = max(map(lambda x: x.width, staves)) if len(staves) > 0 else 1
		max_height = (Config.draw_center*2 + 1) * len(staves) + 30
		tabl_image = Image(width=max_width, height=max_height, 
			background=Color('white'))
		
		#	здесь мы готовим отрисованный титл (будет вверху)
		title = TablMaker.make_title(name, max_width)
		if title is not None:
			tabl_image.composite(title, 0, 0)
			ind = title.height
		else:
			ind = 0
		
		for stave in staves:
			tabl_image.composite(stave, 0, ind)
			ind += (Config.draw_center*2 + 1)
		
		tabl_image.save(filename=out_file)
	
	def make_title(title, width):
		if title is None or title == '':
			return None
		image = Image(width=width, height=30, background=Color('white'))
		with Drawing() as draw:
			draw.font_size = 10
			draw.text(10, 10, title)
			draw.draw(image)
		return image