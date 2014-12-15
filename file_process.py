from service.tabl_maker import TablMaker

lines = open('input.txt')
lines = map(lambda x: x.strip(), lines)
output = TablMaker.process(lines, 'test', 'output/output.png')