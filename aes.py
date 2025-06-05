from Crypto.Cipher import AES 
import binascii 
 
def encryption(aes, P, key): 
    while (len(P) % 16 != 0): 
        P += " " 
    P = P.encode()              # Converts string to binary 
    C = aes.encrypt(P)          # Calls the encrypt function 
    C = binascii.hexlify(C)     # Return the hexadecimal representation of the binary C. 
    C = C.decode()              # Converts binary C to string 
    return C 
 
def decryption(aes, C, key): 
    C = binascii.unhexlify(C)   # Return the binary data represented by the hexadecimal string. 
    P1 = aes.decrypt(C)         # Calls decrypt function 
    P1 = P1.decode().strip()    # Converts binary C to string and remove padding spaces. 
    return P1; 
 
key = input("Enter key: ") 
P = input("Enter plaintext: ") 
print("Plaintext is: ",P) 
key = key.encode()              # key is converted to binary. AES.new() takes the key in binary 
aes_cipher = AES.new(key, AES.MODE_ECB)  # Creates a AES cipher object. 
 

C = encryption(aes_cipher, P, key)      # Calls encryption function with the ciper object, plaintext and key.
print("Ciphertext after encryption: ",C) 
 
P1 = decryption(aes_cipher, C, key)     # Calls decryption function with the ciper object,ciphertext and key. 
print("Plaintext after decryption: ",P1)