class Robot():
	def  __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight

	def introduce_self(self):
		print("My name is " + self.name)



r1 = Robot("refuge", "red", 30)

print (r1.introduce_self())