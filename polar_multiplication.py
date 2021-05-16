import math
import cmath
import numpy

# MAKE SURE SIGNS ARE CORRECT
rad1 = 163
theta1 = -54.048

rad2 = 2.72
theta2 = 54.048

rad_result = rad1 * rad2
theta_result = theta1 + theta2

print(f'Result: {rad_result:.3f}^j{theta_result:.3f}')
print(f'Result in cartesian: {cmath.rect(rad_result, theta_result):.3f}')