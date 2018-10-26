class Robot():
	def  __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight

	def introduce_self(self):
		print("My name is " + self.name)


class Person():
	def __init__(self, name, personality, is_sitting):
		self.name = name
		self.personality = personality
		self.is_sitting = is_sitting

	def sit_down(self):
		self.is_sitting = True

	def stand_up(self):
		self.is_sitting = False
		
r1 = Robot("refuge", "red", 30)

p1 = Person("Wise", "aggresive", False)
p2 = Person("Refuge", "talkative", True)

# p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()