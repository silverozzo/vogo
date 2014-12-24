from guts.config import Config
from service.logger import Logger
from units.image import ImageUnit
from units.note import NoteUnit
from units.overlayed import OverlayedNoteUnit
from units.space import SpaceUnit
from units.tact import TactUnit


image_libary = {
	'tr'  : ('treble_clef.png',           18),
	'tr8' : ('treble_clef_8.png',         18),
	'tr8-': ('treble_clef_8-.png',        18),
	'bc'  : ('bass_clef.png',             18),
	'tc'  : ('tact_c.png',                11),
	'|'   : ('tact_delimeter.png',         5),
	'||'  : ('final.png',                  4),
	':||' : ('repeat_final.png',           7),
	'||:' : ('repeat_start.png',           7),
	'|w'  : ('tact_double_delimeter.png',  5),
	'p04' : ('pause_04.png',              13),
	'p02' : ('pause_02.png',              13),
	'p1'  : ('pause_1.png',               13),
	'p2'  : ('pause_2.png',               13),
	'p4'  : ('pause_4.png',               12),
	'p4.' : ('pause_4_plus.png',          12),
	'p8'  : ('pause_8.png',               12),
	'p8.' : ('pause_8_plus.png',          12),
	'p16' : ('pause_16.png',              12),
	'pp'  : ('pause_play.png',             7),
	'pc'  : ('pause_caesura.png',          6),
}
space_width = {'_' : 4, '__' : 8, '___' : 13}
note_library = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
marker_library = {
	'c': {
			'c-': '1_u',
			'd-': '1_d',
			'e-': '2_u',
			'g-': '2_d',
			'a-': '3_d_b',
			'b-': '3_d',
			'c' : '4_u',
			'd' : '4_d',
			'e' : '5_u',
			'f' : '5_d',
			'g' : '6_u',
			'a' : '6_d',
			'b' : '7_d',
			'c+': '7_u',
			'd+': '8_d',
			'e+': '8_u',
			'f+': '9_d',
			'g+': '9_u',
			'a+': '10_d',
		},
}


class UnitFactory:
	_cur_mark = None
	
	def get(self, letter):
		if letter[0:3] == 'var':
			if letter[3:] not in marker_library:
				Logger.log('unit factory: wrong var: ' + letter)
				return None
			self._cur_mark = letter[3:]
			return None
		if letter == 'novar':
			self._cur_mark = None
			return None
		
		if letter[0] == '_' and letter in space_width:
			return SpaceUnit(space_width[letter])
		
		if letter in image_libary:
			filename = Config.static_unit_dir + image_libary[letter][0]
			return ImageUnit(filename, image_libary[letter][1])
		
		if letter[0] == 't':
			if (len(letter) != 3 or not letter[1].isnumeric() or 
					not letter[2].isnumeric()):
				Logger.log("wrong tact parameters: " + letter)
				return None
			return TactUnit(letter[1], letter[2])
		
		if letter[0] in note_library:
			duration = 1
			if len(letter) > 1 and letter[1].isnumeric():
				duration = int(letter[1])
			if len(letter) > 2 and letter[2].isnumeric():
				duration = int(letter[1:3])
			unit = NoteUnit(letter[0], duration)
			octave = '';
			if '+' in letter:
				unit.set_octave(1)
				octave = '+';
			if '-' in letter:
				unit.set_octave(-1)
				octave = '-';
			if '.' in letter:
				unit.add_dur = True
			if '@' in letter:
				unit.set_alterative('flat')
			if '#' in letter:
				unit.set_alterative('sharp')
			if '$' in letter:
				unit.set_alterative('bekar')
			if '!up' in letter:
				unit.set_forced_rod('up')
			if '!down' in letter:
				unit.set_forced_rod('down')
			if '!!' in letter:
				unit.set_ignore_flag(True)
			if self._cur_mark is not None:
				note = letter[0] + octave
				if note in marker_library[self._cur_mark]:
					unit.set_mark(marker_library[self._cur_mark][note])
				else:
					Logger.log('unknown mark for: ' + note)
			return unit
		
		if letter[0] == 'w':
			over = OverlayedNoteUnit()
			parts = letter[2:].split('*')
			for part in parts:
				chick = self.get(part)
				over.add_note(chick)
			return over
		
		Logger.log('unknown letter: ' + letter)
