'''
@author : Nasrullah
@created : 25.05.2022
@github : github.com/nasdevs
'''

import numpy as np
import sympy as sy
import math
import os

# clear terminal
def clear():
    os.system('clear')

def string_to_matrix(N, x):
    return [list(N[i:i+x]) for i in range(0, len(N), x)]

def char_to_number(N):
    return [[ord(j)-ord('a') for j in i ] for i in N]
    
def number_to_char(N):
    return [[chr(ord('a') + j) for j in i] for i in N]

def mod(N, x):
    return [[j%x for j in i] for i in N]

def encrypt(plaintext, key):
    # C = E(K, P)

    print('\n', '='*5, 'ENCRYPT', '='*5)
    K = string_to_matrix(key, int(math.sqrt(len(key))))
    print(f'\nKey : \n{np.matrix(K)}')
    K = char_to_number(K)
    print(f'\nKey to number : \n{np.matrix(K)}')

    P = string_to_matrix(plaintext, int(math.sqrt(len(key))))
    print(f'\nPlaintext : \n{np.matrix(P)}')
    P = char_to_number(P)
    print(f'\nPlaintext to number : \n{np.matrix(P)}')

    C = np.dot(P, K)
    print(f'\nAfter C = P x K : \n{np.matrix(C)}')
    C = mod(C, 26)
    print(f'\nAfter C mod 26 : \n{np.matrix(C)}')

    C = number_to_char(C)
    print(f'\nMatrix encrypt result : \n{np.matrix(C)}')

    return ''.join(''.join(C[i]) for i in range(len(C)))

def decrypt(cipher, key):
    # P = D(K, C)

    print('\n', '='*5, 'DECRYPT', '='*5)
    K = string_to_matrix(key, int(math.sqrt(len(key))))
    print(f'\nKey : \n{np.matrix(K)}')
    K = char_to_number(K)
    print(f'\nKey to number : \n{np.matrix(K)}')
    
    C = string_to_matrix(cipher, int(math.sqrt(len(key))))
    print(f'\nCiphertext : \n{np.matrix(C)}')
    C = char_to_number(C)
    print(f'\nCiphertext to number : \n{np.matrix(C)}')

    det_K = int(np.linalg.det(K))
    print('\nDeterminant of key : ', det_K)
    det_K = int(np.linalg.det(K) % 26)
    print('After Det K mod 26 : ', det_K)

    invers_K = sy.Matrix(K).adjugate()
    print(f'\nInvers of Key : \n{np.matrix(invers_K)}')
    K = np.multiply(det_K, invers_K)
    print('\nAfter Det K . Invers K : \n', K)
    K = mod(K, 26)
    print(f'\nAfter key mod 26 : \n{np.matrix(K)}')

    P = np.dot(C, K)
    print(f'\nAfter P = C x K : \n{np.matrix(P)}')
    P = mod(P, 26)
    print(f'\nAfter P mod 26 : \n{np.matrix(P)}')
    P = number_to_char(P)
    print(f'\nMatrix decrypt result : \n{np.matrix(P)}')

    return ''.join(''.join(P[i]) for i in range(len(P)))

if __name__ == '__main__':
    clear()

    # statis
    # plaintext = 'nasrullahmakassarmahasis'
    # key = 'UNEXPLAINEDTHING'

    # dinamis (input)
    key = str(input('Input key : '))

    while True:
        plaintext = str(input('Input plaintext : '))
        if len(plaintext) % int(math.sqrt(len(key))) != 0:
            print(f'Jumlah huruf harus kelipatan {int(math.sqrt(len(key)))}, jumlah huruf saat ini {len(plaintext)}')
        else:
            break

    clear()

    print(f'''
Plaintext : {plaintext.lower()}
Key       : {key.lower()}
''')

    cipher_result  = encrypt(plaintext.lower(), key.lower())
    print('\ncipher result :', cipher_result)

    plaintext_result = decrypt(cipher_result, key.lower())
    print('\nplaintext result = ', plaintext_result)

    print(f'''
================= RESULT =================
Plaintext        : {plaintext.lower()}
Key              : {key.lower()}
Cipher result    : {cipher_result}
Plaintext result : {plaintext_result}
''')
