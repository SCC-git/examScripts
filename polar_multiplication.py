import math
import cmath
import numpy

# MAKE SURE SIGNS ARE CORRECT
rad1 = 47.28
theta1 = -9.89

rad2 = 3.09
theta2 = 4.81

rad_result = rad1 * rad2
theta_result = theta1 + theta2

print(f'Result: {rad_result}^j{theta_result}')
print(f'Result in cartesian: {cmath.rect(rad_result, theta_result)}')