'''
@author : nasrullah
@created : 25.05.2022
@github : github.com/nasdevs
'''

import numpy as np
import sympy as sy
import math
import os

def clear():
    os.system('clear')

def string_to_matrix(n, x):
    return [list(n[i:i+x]) for i in range(0, len(n), x)]

def char_to_number(n):
    return [[ord(j)-ord('a') for j in i ] for i in n]
    
def number_to_char(n):
    return [[chr(ord('a') + j) for j in i] for i in n]

def mod(n, x):
    return [[j%x for j in i] for i in n]

def encrypt(plaintext, key):
    k = char_to_number(string_to_matrix(key, int(math.sqrt(len(key)))))
    p = char_to_number(string_to_matrix(plaintext, int(math.sqrt(len(key)))))
    c = number_to_char(mod(np.dot(p, k), 26))

    return ''.join(''.join(c[i]) for i in range(len(c)))


def decrypt(cipher, key):
    c = char_to_number(string_to_matrix(cipher, int(math.sqrt(len(key)))))
    k = mod(np.multiply(int(np.linalg.det(char_to_number(string_to_matrix(key, int(math.sqrt(len(key)))))) % 26), sy.Matrix(char_to_number(string_to_matrix(key, int(math.sqrt(len(key)))))).adjugate()), 26)
    p = number_to_char(mod(np.dot(c, k), 26))

    return ''.join(''.join(p[i]) for i in range(len(p)))

if __name__ == '__main__':
    clear()
    
    key = str(input('input key : '))
    while True:
        plaintext = str(input('input plaintext : '))
        if len(plaintext) % int(math.sqrt(len(key))) != 0:
            print(f'jumlah huruf harus kelipatan {int(math.sqrt(len(key)))}, jumlah huruf saat ini {len(plaintext)}. Anda kelebihan {len(plaintext) % int(math.sqrt(len(key)))} huruf')
        else:
            break

    clear()

    print(f'''
plaintext : {plaintext.lower()}
key       : {key.lower()}
''')

    cipher_result  = encrypt(plaintext.lower(), key.lower())
    plaintext_result = decrypt(cipher_result, key.lower())

    print(f'''
================= result =================
plaintext        : {plaintext.lower()}
key              : {key.lower()}
cipher result    : {cipher_result}
plaintext result : {plaintext_result}
''')
