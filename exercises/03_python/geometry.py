import math

class Point:
	def __init__(self, p1,p2):
		self.p1 = p1
		self.p2 = p2
		
	def distance_form(self,point):
		dist = math.sqrt((point.p1 - self.p1)**2 + (point.p2 - self.p2)**2)
		return dist
		
class Circle:
	def __init__(self,center ,radius):
		self.center = center
		self.radius = radius
	
	def is_inside(self,point):
		if ((point.p1 - self.center.p1) * (point.p1 - self.center.p1) + (point.p2 - self.center.p2) * (point.p2 - self.center.p2) <= self.radius * self.radius):
			return True
		else:
			return False
