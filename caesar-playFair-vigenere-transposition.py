import re
import string
import numpy as np

from string import ascii_uppercase as l


def chiper_text(k, p, c):
    print('Plain Text           : ', p)
    print('Key                  : ', k)
    print('Chiper Text [Result] : ', c)

def plain_text(k, p, c):
    print('Chiper Text          : ', c)
    print('Key                  : ', k)
    print('Plain Text [Result]  : ', p)

class CaesarChiper:
    def __init__(self, k, p='', c=''):
        print('======= Caesar Chiper ========')
        self.a = string.ascii_uppercase
        self.k = k
        self.p = p
        self.c = c

    def encrypt(self):
        print('Encryption')
        self.p = self.p.upper()

        for l in self.p:
            if not l.isalpha():
                self.c += l
                continue

            self.c += self.a[(abs(ord('A') - ord(l)) + self.k) % 26]
        
        chiper_text(self.k, self.p, self.c)

    def decrypt(self):
        print('Decryption')
        self.c = self.c.upper()

        for l in self.c:
            if not l.isalpha():
                self.p += l
                continue

            self.p += self.a[(abs(ord('A') - ord(l)) - self.k) % 26]

        plain_text(self.k, self.p, self.c)

class PlayFairChiper:
    def __init__(self, k, p='', c='', ordo='5x5'):
        print('======= Play Fair Chiper ========')
        self.a = string.ascii_uppercase
        k_temp = k.replace(' ', '').upper()
        self.k = ''
        seen = set()
        for char in k_temp:
            if char not in seen:
                self.k += char
                seen.add(char)
        
        alpha = string.ascii_uppercase
        digits = string.digits
        alpha_digits = alpha+digits

        self.ordo = ordo
        self.p_ori = p.upper()
        self.c_ori = c.upper()
        self.p = re.sub('[^a-zA-Z1-9]', '', p).upper()
        self.c = re.sub('[^a-zA-Z1-9]', '', c).upper()

        if ordo[0] == '5':
            self.table = list(self.k.replace('I', 'J'))
            self.p = self.p.replace('I', 'J')
            self.c = self.c.replace('I', 'J')

            for char in alpha.replace('I', 'J'):
                if char not in self.table:
                    self.table.append(char)
            
            self.table_np = np.array(self.table)

        elif ordo[0] == '6':
            self.table = list(self.k)
            for char in alpha_digits:
                if char not in self.table:
                    self.table.append(char)
            
            self.table_np = np.array(self.table)

        self.table_reshaped = self.table_np.reshape(int(ordo[0]), int(ordo[0]))


    def encrypt(self):
        print(self.table_reshaped)
        group = re.findall('[A-Z0-9]{2}', self.p)
        group += [self.p[-1]+'X'] if len(self.p) % 2 != 0 else []
        for char in group:
            row_A = int((self.table.index(char[0]))/int(self.ordo[0]))
            row_B = int((self.table.index(char[1]))/int(self.ordo[0]))
            
            col_A = self.table.index(char[0]) % int(self.ordo[0])
            col_B = self.table.index(char[1]) % int(self.ordo[0])

            if col_A % (int(self.ordo[0])-1) == 0 and col_B % (int(self.ordo[0])-1) == 0:
                if row_A == row_B and row_A % (int(self.ordo[0])-1) == 0:
                    row_A += 1
                    row_B += 1

                elif row_A % (int(self.ordo[0])-1) == 0:
                    row_A = 0
                    row_B += 1

                elif row_B % (int(self.ordo[0])-1) == 0:
                    row_B = 0
                    row_A += 1
                

            elif col_A % (int(self.ordo[0])-1) == 0:
                col_A = 0
                col_B += 1
            
            elif col_B % (int(self.ordo[0])-1) == 0:
                col_B = 0
                col_A += 1
            
            if row_A % (int(self.ordo[0])-1) == 0:
                row_A = 0
                row_B += 1
            
            elif row_B % (int(self.ordo[0])-1) == 0:
                row_B = 0
                row_A += 1

            print(row_B, col_A, char)
            self.c += self.table_reshaped[row_A, col_B]
            self.c += self.table_reshaped[row_B, col_A]
        
        chiper_text(self.k, self.p, self.c)

    def decrypt(self):
        print(self.table_reshaped)
        print(self.c)
        group = re.findall('[A-Z0-9]{2}', self.c)
        group += [self.c[-1]+'X'] if len(self.c) % 2 != 0 else []

        for char in group:
            row_A = int((self.table.index(char[0]))/int(self.ordo[0]))
            row_B = int((self.table.index(char[1]))/int(self.ordo[0]))
            
            col_A = self.table.index(char[0]) % int(self.ordo[0])
            col_B = self.table.index(char[1]) % int(self.ordo[0])

            if col_A % (int(self.ordo[0])-1) == 0 and col_A != 0:
                row_A = int(self.ordo[0]) - 1
                row_B -= 1
            
            elif col_B % (int(self.ordo[0])-1) == 0 and col_B != 0:
                row_B = int(self.ordo[0]) - 1
                row_A -= 1
            
            if row_A == 0:
                col_A = 0
                col_B -= 1
            
            elif row_B == 0:
                col_B = 0
                col_A -= 1

            self.p += self.table_reshaped[row_A, col_B]
            self.p += self.table_reshaped[row_B, col_A]
        
        plain_text(self.k, self.p, self.c)
        

class VigenereChiper:



    def __init__(self, k, p='', c='', auto=False):
        print('======== Vigenere Chiper =========')
        self.p_ori = p.upper()
        self.c_ori = c.upper()
        self.p = re.sub('[^a-zA-Z]', '', p).upper()
        self.c = re.sub('[^a-zA-Z]', '', c).upper()
        self.k = k.replace(' ', '').upper()

        if auto:
            self.k += self.p[:len(self.p) - len(self.k)] if self.p else self.c[:len(self.c) - len(self.k)]

        else:
            self.k = ''.join([self.k[i%len(self.k)].upper() for i in range(len(self.p if self.p else self.c))])

    def encrypt(self):
        self.c = ''
        i = 0
        for _, l in enumerate(self.p_ori):
            if not l.isalpha():
                self.c += l
                continue

            self.c += chr((ord(self.p[i]) + ord(self.k[i])) % 26 + ord('A'))
            i += 1

        chiper_text(self.k, self.p_ori, self.c)        

    def decrypt(self):
        self.p = ''
        i = 0
        for _, l in enumerate(self.c_ori):
            if not l.isalpha():
                self.p += l
                continue

            self.p += chr((ord(self.c[i]) - ord(self.k[i]) + 26) % 26 + ord('A'))
            i += 1

        plain_text(self.k, self.p, self.c_ori)        

class Transposition:
    def __init__(self, k, p='', c=''):
        print('======== Transposition =========')
        self.p_ori = p.upper()
        self.c_ori = c.upper()
        self.k = k.replace(' ', '').upper()
        self.k_sorted = list(map(int, list(self.k)))
        self.k_sorted.sort()

        self.p = p.replace(' ', '').upper()
        self.c = c.replace(' ', '').upper()

        if len(self.p) % len(self.k) != 0:
            self.p += string.ascii_uppercase[-(len(self.p) % len(self.k)-1):]

        elif len(self.c) % len(self.k) != 0:
            self.c += string.ascii_uppercase[-(len(self.c) % len(self.k)-1):]
        
        if self.p:
            self.p_np = np.array(list(self.p))
            self.p_np = self.p_np.reshape(round(len(self.p) / len(self.k)), len(self.k))

            self.p_dict = {}

            for i in self.k:
                lst_letters = []
                for elm in range(len(self.p_np)):
                    lst_letters.append(self.p_np[elm, self.k.index(str(i))])
                
                self.p_dict[str(i)] = lst_letters
        
        elif self.c:
            self.c_dict = {}

            temp = re.findall('.{'+str(len(self.c)//len(self.k))+'}', self.c)
            for i, elm in enumerate(self.k_sorted):
                self.c_dict[str(elm)] = temp[i]
    
    def encrypt(self):
        for i in self.k_sorted:
            self.c += ''.join(self.p_dict[str(i)])
        
        chiper_text(self.k, self.p, self.c)

    def decrypt(self):
        for i in range(len(self.c) // len(self.k)):
            for j in self.k:
                self.p += self.c_dict[j][i]
        
        plain_text(self.k, self.p, self.c)
    
if __name__ == '__main__':
    caesarChiper = CaesarChiper(123098, c='')
    # caesarChiper.encrypt()
    caesarChiper.decrypt()

    # # Failed
    # playFairChiper = PlayFairChiper('FAILED', p='', ordo='5')
    # playFairChiper.encrypt()
    # playFairChiper.decrypt()

    vigenereChiper = VigenereChiper('bismillah', p='', auto=True)
    vigenereChiper.encrypt()
    # vigenereChiper.decrypt()

    
    transposition = Transposition('5281936074', c='')
    # transposition.encrypt()
    transposition.decrypt()
