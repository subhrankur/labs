import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi_n):
    # Extended Euclidean Algorithm for modular inverse
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

    g, x, _ = egcd(e, phi_n)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi_n

def key_generation():
    p = int(input('Enter 1st large prime p: '))
    q = int(input('Enter 2nd large prime q: '))
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = int(input(f'Enter e (1 < e < {phi_n}) such that gcd(e, phi_n) = 1: '))
    while gcd(e, phi_n) != 1 or not (1 < e < phi_n):
        e = int(input(f'Invalid e. Enter again (1 < e < {phi_n}): '))

    d = modinv(e, phi_n)
    return e, n, d

def encrypt(P, e, n):
    return pow(P, e, n)

def decrypt(C, d, n):
    return pow(C, d, n)

# Key generation
e, n, d = key_generation()
print(f'Public Key: (e={e}, n={n})')
print(f'Private Key: d={d}')

# Encrypt & decrypt integer
P = int(input('Enter plaintext (integer): '))
C = encrypt(P, e, n)
print(f'Ciphertext = {C}')
P1 = decrypt(C, d, n)
print(f'Decrypted plaintext = {P1}')

# Encrypt & decrypt alphabetic message
PP = input('Enter plaintext (letters only): ')
PP = PP.lower().replace(" ", "")
print(f'Normalized Plaintext: {PP}')

# Encrypt
CC_list = [encrypt(ord(ch) - ord('a'), e, n) for ch in PP]
print('Ciphertext (numeric list):', CC_list)

# Concatenated ciphertext string (not secure format, for demo)
CC = ''.join(str(c) for c in CC_list)
print(f'Concatenated Ciphertext = {CC}')

# Decrypt
PP1 = ''.join(chr(decrypt(c, d, n) + ord('a')) for c in CC_list)
print(f'Decrypted Plaintext = {PP1}')
