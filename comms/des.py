# VALUES TO CHANGE START ON LINE 260

p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
ip = [2, 6, 3, 1, 4, 8, 5, 7]
ip_inverse = [4, 1, 3, 5, 7, 2, 8, 6]
expansion = [4, 1, 2, 3, 2, 3, 4, 1]

s0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

s1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

p4 = [2, 4, 3, 1]


def put_through_blocks(mode, input_to_ip, first_fk_key, second_fk_key):

    print('\nFIRST HALF OF FK\n')

    if mode == 'cbc' and encode:
        input_to_ip = ['0' if input_to_ip[i] == prev_bits[i] else '1' for i, value in enumerate(input_to_ip)]
    elif mode == 'cfm':
        actual_plaintext = input_to_ip
        input_to_ip = prev_bits

    storage_vector = [69, 69, 69, 69, 69, 69, 69, 69]
    for index, value in enumerate(ip):
        storage_vector[index] = input_to_ip[value - 1]
    print(f'After IP: {storage_vector}')

    first_half = storage_vector[0: int((len(storage_vector)/2))]
    second_half = storage_vector[int((len(storage_vector)/2)) : int(len(storage_vector))]

    storage_vector = [69, 69, 69, 69, 69, 69, 69, 69]
    for index, value in enumerate(expansion):
        storage_vector[index] = second_half[value - 1]
    print(f'After EP: {storage_vector}')

    for index, value in enumerate(storage_vector):
        if storage_vector[index] == first_fk_key[index]:
            storage_vector[index] = '0'
        else:
            storage_vector[index] = '1'
    print(f'After XOR with first key: {storage_vector}')

    s0_half = storage_vector[0: int((len(storage_vector)/2))]
    s1_half = storage_vector[int((len(storage_vector)/2)) : int(len(storage_vector))]

    s0_row = int(s0_half[0] + s0_half[3], 2)
    s0_col = int(s0_half[1] + s0_half[2], 2)

    s1_row = int(s1_half[0] + s1_half[3], 2)
    s1_col = int(s1_half[1] + s1_half[2], 2)

    s0_value = "{:02b}".format(s0[s0_row][s0_col])
    s1_value = "{:02b}".format(s1[s1_row][s1_col])

    print(f'S0 Value = {s0_value}')
    print(f'S1 Value = {s1_value}')

    s0_value = list(s0_value)
    s1_value = list(s1_value)
    s0_value.extend(s1_value)

    storage_vector = [69, 69, 69, 69]
    for index, value in enumerate(p4):
        storage_vector[index] = s0_value[value - 1]
    print(f'After P4: {storage_vector}')

    for index, value in enumerate(storage_vector):
        if storage_vector[index] == first_half[index]:
            storage_vector[index] = '0'
        else:
            storage_vector[index] = '1'
    print(f'After XOR with first half: {storage_vector}')

    second_half.extend(storage_vector)
    swap = second_half
    print(f'After Swap: {second_half}')

    print('\nSECOND HALF OF FK\n')

    storage_vector = swap

    first_half = storage_vector[0: int((len(storage_vector)/2))]
    second_half = storage_vector[int((len(storage_vector)/2)) : int(len(storage_vector))]

    storage_vector = [69, 69, 69, 69, 69, 69, 69, 69]
    for index, value in enumerate(expansion):
        storage_vector[index] = second_half[value - 1]
    print(f'After EP: {storage_vector}')

    for index, value in enumerate(storage_vector):
        if storage_vector[index] == second_fk_key[index]:
            storage_vector[index] = '0'
        else:
            storage_vector[index] = '1'
    print(f'After XOR with second key: {storage_vector}')

    s0_half = storage_vector[0: int((len(storage_vector)/2))]
    s1_half = storage_vector[int((len(storage_vector)/2)) : int(len(storage_vector))]

    s0_row = int(s0_half[0] + s0_half[3], 2)
    s0_col = int(s0_half[1] + s0_half[2], 2)

    s1_row = int(s1_half[0] + s1_half[3], 2)
    s1_col = int(s1_half[1] + s1_half[2], 2)

    s0_value = "{:02b}".format(s0[s0_row][s0_col])
    s1_value = "{:02b}".format(s1[s1_row][s1_col])

    print(f'S0 Value = {s0_value}')
    print(f'S1 Value = {s1_value}')

    s0_value = list(s0_value)
    s1_value = list(s1_value)
    s0_value.extend(s1_value)

    storage_vector = [69, 69, 69, 69]
    for index, value in enumerate(p4):
        storage_vector[index] = s0_value[value - 1]
    print(f'After P4: {storage_vector}')

    for index, value in enumerate(storage_vector):
        if storage_vector[index] == first_half[index]:
            storage_vector[index] = '0'
        else:
            storage_vector[index] = '1'
    print(f'After XOR with first half: {storage_vector}')

    storage_vector.extend(second_half)

    result = [69, 69, 69, 69, 69, 69, 69, 69]

    for index, value in enumerate(ip_inverse):
        result[index] = storage_vector[value - 1]

    if mode == 'cbc' and not encode:
        result = ['0' if result[i] == prev_bits[i] else '1' for i,value in enumerate(result)]
    elif mode == 'cfm':
        result = ['0' if result[i] == actual_plaintext[i] else '1' for i,value in enumerate(result)]

    print(f'\nRESULT: {result}')



if __name__ == '__main__':
    eight_bit_plaintext = '10101010' # Put the plaintext in here if encoding/ Ciphertext if decoding
    ten_bit_key = '0011110101'
    prev = '10110100'
    ecm_or_cbc_or_what = 'cfm' # 'ecm' 'cbc' 'cfm'
    encode = False

    if ecm_or_cbc_or_what == 'cfm':
        encode = True

    plaintext_bits = list(eight_bit_plaintext)
    key_bits = list(ten_bit_key)
    prev_bits = list(prev)

    if len(plaintext_bits) != 8:
        print(f'Plaintext length incorrect ({len(plaintext_bits)})')
    if len(key_bits) != 10:
        print(f'Key length incorrect ({len(key_bits)})')
    if len(plaintext_bits) != len(prev_bits):
        print(f'Plaintext length different to previous ({len(plaintext_bits)} vs. {len(prev_bits)})')

    print('KEYS:')

    temp = [69, 69, 69, 69, 69, 69, 69, 69, 69, 69]
    # GETTING K1
    for index, value in enumerate(key_bits):
        temp[index] = key_bits[p10[index] - 1]
    print(f'After P10: {temp}')

    lcs1a = temp[0: int((len(temp)/2))]
    lcs1b = temp[int((len(temp)/2)) : int(len(temp))]

    lcs1a.append(lcs1a.pop(0))
    lcs1b.append(lcs1b.pop(0))

    lcs1a.extend(lcs1b)
    lcs1 = lcs1a
    print(f'After LCS1: {lcs1}')

    k1 = [69, 69, 69, 69, 69, 69, 69, 69]
    for index, value in enumerate(p8):
        k1[index] = lcs1[value - 1]
    print(f'After P8, K1: {k1}')

    lcs2a = lcs1[0: int((len(lcs1)/2))]
    lcs2b = lcs1[int((len(lcs1)/2)) : int(len(lcs1))]

    lcs2a.append(lcs2a.pop(0))
    lcs2b.append(lcs2b.pop(0))

    lcs2a.extend(lcs2b)
    lcs2 = lcs2a
    print(f'After LCS2: {lcs2}')

    k2 = [69, 69, 69, 69, 69, 69, 69, 69]
    for index, value in enumerate(p8):
        k2[index] = lcs2[value - 1]
    print(f'After P8, K2: {k2}')

    if encode:
        put_through_blocks(ecm_or_cbc_or_what, plaintext_bits, k1, k2)
    else:
        put_through_blocks(ecm_or_cbc_or_what, plaintext_bits, k2, k1)
