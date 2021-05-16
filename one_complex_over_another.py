import math
import cmath
import numpy

numerator = 300
denominator = complex(96.58, -8.12)

result = numerator / denominator

print(f'Numerator: {numerator:.3f}')
print(f'Denominator: {denominator:.3f}')
print(f'Result: {result:.3f}')
print(f'Result in polar form (radians): {cmath.polar(result)}')
print(f'Result in polar form (degrees): {abs(result):.3f}^j{numpy.degrees(cmath.phase(result)):.3f}')