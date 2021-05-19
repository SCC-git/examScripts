import math
import cmath
import numpy as np

relative_mu = 5
freq = 1 * 10**9
epsilon_relative = 30
sigma = 0.0025  # the one in units S/m
impedance1 = 120 * math.pi  # Impedance of material one (default for air)

GOOD_CONDUCTOR_THRESHOLD = 100 # Can change if you want
LOW_LOSS_MEDIUM_THRESHOLD = 0.01

omega = 2 * math.pi * freq
epsilon_dash_dash = sigma / omega
epsilon_dash = epsilon_relative * 8.85 * 10**-12

thresh = epsilon_dash_dash / epsilon_dash

alpha = 0
beta = 0
impedance2 = 0

if (thresh > GOOD_CONDUCTOR_THRESHOLD):
    print(f"GOOD CONDUCTOR (epsilon''/epsilon' = {thresh})")
    alpha = np.sqrt(math.pi * freq * relative_mu * (4 * math.pi * 10**-7) * sigma)
    beta = alpha
    impedance2 = complex(alpha/sigma, alpha/sigma)
elif (thresh < LOW_LOSS_MEDIUM_THRESHOLD):
    print(f"LOW LOSS MEDIUM (epsilon''/epsilon' = {thresh})")
    alpha = (sigma / 2) * np.sqrt((relative_mu * (4 * math.pi * 10**-7)) / (epsilon_relative * 8.854 * 10**-12))
    beta = omega * np.sqrt((relative_mu * (4 * math.pi * 10**-7)) * (epsilon_relative * 8.854 * 10**-12))
    impedance2 = np.sqrt((relative_mu * (4 * math.pi * 10**-7)) / (epsilon_relative * 8.854 * 10**-12))
elif(sigma == 0):
    print(f"LOSSLESS MEDIUM (epsilon''/epsilon' = {thresh})")
    alpha = 0
    beta = omega * np.sqrt((relative_mu * (4 * math.pi * 10**-7)) * (epsilon_relative * 8.854 * 10**-12))
    impedance2 = np.sqrt((relative_mu * (4 * math.pi * 10**-7)) / (epsilon_relative * 8.854 * 10**-12))
else:
    print(f"USE THE GENERAL FORMULA FILE (quasi something: (epsilon''/epsilon' = {thresh}))")

refl_coefficient = (impedance2 - impedance1) / (impedance2 + impedance1)
tau = refl_coefficient + 1

print(f'Alpha: {alpha}')
print(f'Beta: {beta}')
print(f'Impedance2: {impedance2:.3f}')
print(f'Reflection coefficient: {refl_coefficient:.3f}')
print(f'Tau: {tau:.3f}')