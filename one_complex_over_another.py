import math
import cmath
import numpy

numerator = 300
denominator = complex(96.58, -8.12)

result = numerator / denominator

print(f'Numerator: {numerator}')
print(f'Denominator: {denominator}')
print(f'Result: {result}')
print(f'Result in polar form (radians): {cmath.polar(result)}')
print(f'Result in polar form (degrees): {abs(result)}^j{numpy.degrees(cmath.phase(result))}')