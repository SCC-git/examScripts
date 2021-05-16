import math
import cmath
import numpy

radians = True # set true if theta already in radians

rad1 = 1
theta1 = 0.3 * math.pi

rad2 = 0.09
theta2 = -0.3 * math.pi

if radians:
    rect1 = cmath.rect(rad1, theta1)
    rect2 = cmath.rect(rad2, theta2)
else:
    rect1 = cmath.rect(rad1, math.radians(theta1))
    rect2 = cmath.rect(rad2, math.radians(theta2))

result = rect1 + rect2

print(f'Result in rectangular form: {result:.3f}')
print(f'Result in polar form (radians): {cmath.polar(result)}')
print(f'Result in polar form (degrees): {abs(result):.3f}^j{numpy.degrees(cmath.phase(result)):.3f}')