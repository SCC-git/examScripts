import math
import cmath
import numpy

# MAKE SURE SIGNS ARE CORRECT
rad1 = 146.095
theta1 = -5.08

rad2 = 0.9759
theta2 = 48.968

rad_result = rad1 / rad2
theta_result = theta1 - theta2

print(f'Result: {rad_result:.3f}^j{theta_result:.3f}')
print(f'Result in cartesian: {cmath.rect(rad_result, theta_result):.3f}')