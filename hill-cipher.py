'''
@author : nasrullah
@created : 25.05.2022
@github : github.com/nasdevs
'''

import numpy as np
import sympy as sy
import math
from os import system

class Hill_Cipher:
    def string_to_matrix(n, x):
        return [list(n[i:i+x]) for i in range(0, len(n), x)]

    def char_to_number(n):
        return np.array([[ord(j)-ord('a') for j in i ] for i in n])
        
    def number_to_char(n):
        return [[chr(ord('a') + j) for j in i] for i in n]

    def encrypt(plaintext, key):
        K = Hill_Cipher.char_to_number(Hill_Cipher.string_to_matrix(key, int(math.sqrt(len(key)))))
        P = Hill_Cipher.char_to_number(Hill_Cipher.string_to_matrix(plaintext, int(math.sqrt(len(key)))))
        C = Hill_Cipher.number_to_char(np.dot(P, K) % 26)

        return ''.join(''.join(C[i]) for i in range(len(C)))

    def decrypt(cipher, key):
        C = Hill_Cipher.char_to_number(Hill_Cipher.string_to_matrix(cipher, int(math.sqrt(len(key)))))
        K_det = int(np.linalg.det(Hill_Cipher.char_to_number(Hill_Cipher.string_to_matrix(key, int(math.sqrt(len(key)))))) % 26)
        try:
            K_modular = [(K_det * i) % 26 for i in range(26)].index(1, 0, 26)
        except:
            print('key does not have a modular multiplicative inverse.\nPlease use another key.')
            exit()
        K = np.multiply(K_modular, sy.Matrix(Hill_Cipher.char_to_number(Hill_Cipher.string_to_matrix(key, int(math.sqrt(len(key)))))).adjugate()) % 26
        P = Hill_Cipher.number_to_char(np.dot(C, K) % 26)

        return ''.join(''.join(P[i]) for i in range(len(P)))

if __name__ == '__main__':
    system('clear')

    while True:
        key = str(input('input key : '))
        if math.sqrt(len(key)) not in range(1, 101):
            print(f'number of letters has no integer root, current number of letters {len(key)} and resulting root {round(math.sqrt(len(key)), 5)}')
        else:
            break

    while True:
        plaintext = str(input('input plaintext : '))
        if len(plaintext) % int(math.sqrt(len(key))) != 0:
            print(f'number of letters must be a multiple of {int(math.sqrt(len(key)))}, the current number of letters is {len(plaintext)}. You are excess {len(plaintext) % int(math.sqrt(len(key)))} letters')
        else:
            break

    system('clear')

    encrypt = Hill_Cipher.encrypt(plaintext.lower(), key.lower())
    decrypt = Hill_Cipher.decrypt(encrypt, key.lower())

    print(f'''
============= result =============
plaintext : {plaintext.lower()}
key       : {key.lower()}
encrypt   : {encrypt}
decrypt   : {decrypt}
''')
