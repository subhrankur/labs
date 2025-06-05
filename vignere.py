def encrypt(p, k):
    return ''.join(chr((ord(p[i]) - 97 + ord(k[i % len(k)]) - 97) % 26 + 65) for i in range(len(p)))

def decrypt(c, k):
    return ''.join(chr((ord(c[i]) - 65 - (ord(k[i % len(k)]) - 97) + 26) % 26 + 97) for i in range(len(c)))

p = input("Input Plaintext:").lower().replace(" ", "")
k = input("Input Key:").lower().replace(" ", "")
print("Plaintext:", p)
print("Key:", k)

c = encrypt(p, k)
print("Encrypted Ciphertext:", c)

d = decrypt(c, k)
print("Decrypted Plaintext:", d)
