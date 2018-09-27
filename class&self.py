class Human():
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def speak_name(self):
		print "My name is %s" % self.firstname, self.lastname

	def perform_math_task(self, math_operation, *args):
		print "%s results is: %f" % (self.firstname, math_operation(*args))

def add(a, b):
	return a + b

will = Human("refuge", "wise")

will.perform_math_task(add, 40, 50)



# will = Human("refuge", "wise")

# print will.firstname
# print will.lastname

# will.speak_name()