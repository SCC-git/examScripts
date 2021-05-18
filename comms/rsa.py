e = 25
n = 221
c = 2


# def not stolen
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


if __name__ == '__main__':
    factors = prime_factors(n)
    p = 0
    q = 0
    correct_answer = False

    print('PRIME FACTORS')
    for i in range(0, len(factors)):
        for j in range(1, len(factors)):
            product = factors[i] * factors[j]
            if (product == n):
                p = factors[i]
                q = factors[j]
            print(f'{factors[i]} * {factors[j]} = {product} ({True if product == n else False})')

    mod_for_d = (p - 1) * (q - 1)

    print(f'\np={p}, q={q}')
    print('d = e^-1 mod (p-1)(q-1)')
    print(f'd = 1/{e} mod {mod_for_d}')
    print(f'{e}d = 1 mod {mod_for_d}')
    print(f'i.e. {e}d - 1 = k({mod_for_d})\n')

    d = 0
    multiple_of_mod = 0
    for i in range(30):
        multiple_of_mod = i * mod_for_d
        multiple_of_mod_plus_one = multiple_of_mod + 1
        if multiple_of_mod_plus_one % e == 0 and d == 0:
            d = int(multiple_of_mod_plus_one / e)
        print(f'{i} * {mod_for_d} = {multiple_of_mod}, {multiple_of_mod} + 1 = {multiple_of_mod_plus_one}, Divisible by e = {True if multiple_of_mod_plus_one % e == 0 else False} ({multiple_of_mod_plus_one}/{e}={multiple_of_mod_plus_one/e})')
    print(f'PRIVATE D = {d}')

    print('\nDECIPHERING CIPHER TEXT:')
    print('m = c^d mod n')
    print(f'm = {c}^{d} mod {n}')
    print(f'Answer = {pow(c, d, n)}')