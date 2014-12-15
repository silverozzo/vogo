from units.base_unit import BaseUnit


class SpaceUnit(BaseUnit):
	def __init__(self, width):
		self._width = width
	
	def get_unit_width(self):
		return self._width
