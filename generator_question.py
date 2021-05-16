import math
import cmath
import numpy

z_zero = 50
z_load = 75
length = 0.15                    # wavelengths

z_generator = 50 # if given
v_generator = 300 # if given

beta_l = (2 * math.pi) * length

input_impedance = (z_zero * complex(z_load, z_zero * math.tan(beta_l))) / complex(z_zero, z_load*math.tan(beta_l))

i_in = v_generator / (z_generator + input_impedance)

i_in_star = complex(i_in.real, -i_in.imag)

v_in = i_in * input_impedance

p_in = 0.5 * (v_in * i_in_star).real

refl_coefficient = (z_load - z_zero) / (z_load + z_zero)

v_zero_plus = v_in * (1 / (cmath.rect(1, beta_l) + complex(abs(refl_coefficient), cmath.phase(refl_coefficient) - beta_l)))

v_load = v_zero_plus * (1 + refl_coefficient)

i_load = (v_zero_plus / z_zero) * (1 - refl_coefficient)

i_load_star = complex(i_load.real, -i_load.imag)

p_load = 0.5 * (v_load * i_load_star).real

p_generator = 0.5 * (v_generator * i_in).real

p_z_generator = 0.5 * (abs(i_in) ** 2) * z_generator

print('IN RECTANGULAR:')
print(f'Zin: {input_impedance:.3f} Ohms')
print(f'Iin: {i_in:.3f} A')
print(f'Vin: {v_in:.3f} V')
print(f'Pin: {p_in:.3f} W')
print(f'Reflection coefficient: {refl_coefficient:.3f}')
print(f'V0+: {v_zero_plus:.3f} V')
print(f'Vload: {v_load:.3f} V')
print(f'Iload: {i_load:.3f} A')
print(f'Iload*: {i_load_star:.3f} A')
print(f'Pload: {p_load:.3f} W')
print(f'Pgenerator: {p_generator:.3f} W')
print(f'P_z_generator: {p_z_generator:.3f} W')

print('\nIN POLAR (degrees):')
print(f'Zin: {abs(input_impedance):.3f}^j{numpy.degrees(cmath.phase(input_impedance)):.3f} Ohms')
print(f'Iin: {abs(i_in):.3f}^j{numpy.degrees(cmath.phase(i_in)):.3f} A')
print(f'Vin: {abs(v_in):.3f}^j{numpy.degrees(cmath.phase(v_in)):.3f} V')
print(f'Pin: {abs(p_in):.3f}^j{numpy.degrees(cmath.phase(p_in)):.3f} W')
print(f'Reflection coefficient: {abs(refl_coefficient):.3f}^j{numpy.degrees(cmath.phase(refl_coefficient)):.3f}')
print(f'V0+: {abs(v_zero_plus):.3f}^j{numpy.degrees(cmath.phase(v_zero_plus)):.3f} V')
print(f'Vload: {abs(v_load):.3f}^j{numpy.degrees(cmath.phase(v_load)):.3f} V')
print(f'Iload: {abs(i_load):.3f}^j{numpy.degrees(cmath.phase(i_load)):.3f} A')
print(f'Iload*: {abs(i_load_star):.3f}^j{numpy.degrees(cmath.phase(i_load_star)):.3f} A')
print(f'Pload: {abs(p_load):.3f}^j{numpy.degrees(cmath.phase(p_load)):.3f} W')
print(f'Pgenerator: {abs(p_generator):.3f}^j{numpy.degrees(cmath.phase(p_generator)):.3f} W')
print(f'P_z_generator: {abs(p_z_generator):.3f}^j{numpy.degrees(cmath.phase(p_z_generator)):.3f} W')

print('\nIF LOSSLESS:')
print(f'Pin = Pload: {p_in:.3f} = {p_load:.3f}')
print(f'Pgenerator = P_z_generator + Pin: {p_generator:.3f} = {p_z_generator:.3f} + {p_in:.3f} (={p_z_generator + p_in:.3f})')