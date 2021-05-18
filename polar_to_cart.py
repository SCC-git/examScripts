
# Converting Polar Coordinate to Cartesian Coordinates
# Importing math library
import math

array = [[0.95,0.2],[0.80,0.4],[0.75,0.6],[0.6,0.75]]

for x in array:
	# Reading radius and angle of polar coordinate
	radius = x[0]

	# Converting theta from degree to radian
	theta = x[1] * math.pi
	negtheta = -x[1] * math.pi

	# Converting polar to cartesian coordinates
	x1 = radius * math.cos(theta)
	y1 = radius * math.sin(theta)
	x2 = radius * math.cos(negtheta)
	y2 = radius * math.sin(negtheta)

	# Displaying cartesian coordinates
	print('Cartesian coordinate is: (x = %0.2f, y = %0.2f)' %(x1,y1))
	print('Cartesian coordinate is: (x = %0.2f, y = %0.2f)' %(x2,y2))
	print()