import math
import cmath
import numpy

z_zero = 50
z_load = 60
length = 0.15                    # wavelengths

numerator = complex(z_load, z_zero * math.tan((2 * math.pi) * length))

denominator = complex(z_zero, z_load*math.tan((2 * math.pi) * length))

top_over_bottom = numerator / denominator

result = (z_zero * numerator) / denominator

print(f'Numerator: {numerator}')
print(f'Denominator: {denominator}')
print(f'Top over bottom: {top_over_bottom}')
print(f'Result: {result}')
print(f'Result in polar form (radians): {cmath.polar(result)}')
print(f'Result in polar form (degrees): {abs(result)}^j{numpy.degrees(cmath.phase(result))}')