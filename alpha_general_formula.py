import math
import cmath
import numpy

relative_mu = 1
freq = 200 * 10**6
epsilon_relative = 4
sigma = 0.1  # the one in units S/m
impedance1 = 120 * math.pi  # Impedance of material one (default for air)

mu = relative_mu * 4 * math.pi * 10**-7
omega = 2 * math.pi * freq
epsilon_dash_dash = sigma / omega
epsilon_dash = epsilon_relative * 8.85 * 10**-12

test = (mu * epsilon_dash) / 2

alpha = omega * math.sqrt(((mu * epsilon_dash) / 2) * (math.sqrt(1 + (epsilon_dash_dash / epsilon_dash) ** 2) - 1))
beta = omega * math.sqrt(((mu * epsilon_dash) / 2) * (math.sqrt(1 + (epsilon_dash_dash / epsilon_dash) ** 2) + 1))
impedance2 = math.sqrt(mu / epsilon_dash) * (complex(1, -(epsilon_dash_dash / epsilon_dash)))**-0.5

refl_coefficient = (impedance2 - impedance1) / (impedance2 + impedance1)
tau = refl_coefficient + 1

print('ALPHA')
print(f'EQUATION: {omega:.3f}[ {mu:.3f}*{epsilon_dash:.3f}/2 [ sqrt(1 + ({epsilon_dash_dash:.3f}/{epsilon_dash:.3f})^2) ]-1] ^ (1/2)')
print(f'SOME CALCULATED: {omega:.3f}[ {mu*epsilon_dash/2} [ sqrt(1 + {(epsilon_dash_dash/epsilon_dash)**2:.3f}) ]-1] ^ (1/2)')
print(f'ALPHA: {alpha:.3f}')

print('\nBETA')
print(f'EQUATION: {omega:.3f}[ {mu:.3f}*{epsilon_dash:.3f}/2 [ sqrt(1 + ({epsilon_dash_dash:.3f}/{epsilon_dash:.3f})^2) ]+1] ^ (1/2)')
print(f'SOME CALCULATED: {omega:.3f}[ {mu*epsilon_dash/2:.3f} [ sqrt(1 + {(epsilon_dash_dash/epsilon_dash)**2:.3f}) ]+1] ^ (1/2)')
print(f'BETA: {beta:.3f}')

print('\nIMPEDANCE')
print(f'IMPEDANCE: {impedance2:.3f}')

print('\nREFLECTION COEFFICIENT')
print(f'REFLECTION COEFFICIENT: {refl_coefficient:.3f}')
print(f'REFLECTION COEFFICIENT (polar): {cmath.polar(refl_coefficient)}')
print(f'REFLECTION COEFFICIENT (polar, degrees): {abs(refl_coefficient):.3f}^j{numpy.degrees(cmath.phase(refl_coefficient)):.3f}')

print('\nTAU')
print(f'TAU: {tau:.3f}')
print(f'TAU (polar): {cmath.polar(tau)}')
print(f'TAU (polar, degrees): {abs(tau):.3f}^j{numpy.degrees(cmath.phase(tau)):.3f}')

