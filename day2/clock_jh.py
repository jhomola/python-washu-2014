class Clock():
	def __init__(self, hours, minutes=0):
		self.hours = hours
		self.minutes1 = hours*60
		self.minutes2 = minutes
	
	@classmethod
	def at(cls, hours, minutes=0):
		return cls(hours, minutes)
		
	def __str__(self):
		return "%02d:%02d" % (self.hours, self.minutes2)
		
	def __add__(self, other):
		time = self.minutes1 + self.minutes2 + other
		time1 = time / 60
		time2 = time % 60
		if time<1400:
			return "%02d:%02d" % (time1, time2)
		else:
			time1 = time1 - 24
			return "%02d:%02d" % (time1, time2)
			
		
	def __sub__(self, other):
		time = self.minutes1 + self.minutes2 - other
		time1 = time / 60
		time2 = time % 60
		if time>-1:
			return "%02d:%02d" % (time1, time2)
		else:
			time1 = time1 + 24
			return "%02d:%02d" % (time1, time2)
		
		

		
		
a = Clock(3,14)
print a

b = Clock.at(3,16)
print b

c = Clock.at(3,14) + 5
print c

d = Clock.at(3,14) + 50
print d

e = Clock.at(3,14) - 5
print e

f = Clock.at(3,14) - 50
print f

g = Clock.at(23,14) + 50
print g

h = Clock.at(00,15) - 30
print h