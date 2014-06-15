import numpy

class Option:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.data = numpy.zeros((x,y),dtype=bool_)
		
