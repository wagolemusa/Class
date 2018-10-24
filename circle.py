from math import pi

def circle_area(r):
	return pi*(r**2)

radii = [2,0, -3, 2 + 5j, True, 10]
message = "Area of circle with r = {radius} is {area}."

for r in radii:
	A = circle_area(r)
	print(message.format(radius=r, area=A))