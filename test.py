from guts.config import Config
from service.line_maker import LineMaker
from service.tabl_maker import TablMaker
from units.base_unit import BaseUnit

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


check = 'tr t34 c4 d4 e4'
result = LineMaker.process(check)
result.save(filename='test.png')

check = 'tr [!down (!up b8 a8 ) ]'
result = LineMaker.process(check)
result.save(filename='test.png')


check = 'tr varc c4 d4 e4 novar'
result = LineMaker.process(check)
result.save(filename='test_mark.png')

check = ['tr t34 c4 d4 e4', 'tr f4 g4 a4']
result = TablMaker.process(check, 'test', 'test2.png')

check = 'tr c0#'
result = LineMaker.process(check)
result.save(filename='test_empty.png')

check = 'tr 333 c1 d1 e1'
result = LineMaker.process(check)
result.save(filename='test_trip.png')

from service.logger import Logger
Logger.log('foobar')
print(Logger.get())
