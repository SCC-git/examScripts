import math

omega = 4 * math.pi * 10**8
relative_epsilon = 4
mu = 1
epsilon_dash = omega * relative_epsilon * 8.85 * 10**-12
epsilon_dash_dash = 0.1

result = omega * math.sqrt(((mu * epsilon_dash) / 2) * (math.sqrt(1 + (epsilon_dash_dash / epsilon_dash) ** 2) - 1))

print(f'EQUATION: {omega}[ {mu}*{epsilon_dash}/2 [ sqrt(1 + ({epsilon_dash_dash}/{epsilon_dash})^2) ]-1] ^ (1/2)')
print(f'SOME CALCULATED: {omega}[ {mu*epsilon_dash/2} [ sqrt(1 + {(epsilon_dash_dash/epsilon_dash)**2}) ]-1] ^ (1/2)')
print(f'RESULT: {result}')