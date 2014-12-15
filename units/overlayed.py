from guts.config import Config
from units.base_unit import BaseUnit
from units.note import NoteUnit


class OverlayedNoteUnit(BaseUnit):
	_notes = []
	
	def __init__(self):
		self._notes = []
	
	def print_explode(self, level=0):
		lev_offset = "\t" * (level)
		print(lev_offset + "OvelayedNoteUnit:")
		lev_offset = "\t" * (level+1)
		for note in self._notes:
			note.print_explode(level + 1)
	
	def draw(self, stave_image):
		for note in self._notes:
			note.set_line_offset(self._line_offset)
			note.draw(stave_image)
	
	def get_unit_width(self):
		if len(self._notes) > 0:
			return self._notes[0].get_unit_width()
		return 0
	
	def add_note(self, note):
		self._notes.append(note)
	
	def set_knit(self, knit):
		for note in self._notes:
			note.set_knit(knit)
	
	def get_stave_offset(self, for_knit=None):
		if for_knit not in ['min', 'max']:
			return self._notes[0].get_stave_offset()
		
		min, max = None, None
		for note in self._notes:
			cur = note.get_stave_offset()
			if min is None or min > cur:
				min = cur
			if max is None or max < cur:
				max = cur
		if for_knit == 'min':
			return min
		if for_knit == 'max':
			return max
		return None
	
	def set_rod_length(self, length):
		for note in self._notes:
			note.set_rod_length(length)