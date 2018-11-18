import math

class Point:
	def __init__(self, p1,p2):
		self.x = p1
		self.y = p2
		
	def distance_from(self,point):
		dist = math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
		return dist
		
class Circle:
	def __init__(self,center ,radius):
		self.center = center
		self.radius = radius
	
	def is_inside(self,point):
		if ((point.x - self.center.x) * (point.x - self.center.x) + (point.y - self.center.y) * (point.y - self.center.y) <= self.radius * self.radius):
			return True
		else:
			return False
