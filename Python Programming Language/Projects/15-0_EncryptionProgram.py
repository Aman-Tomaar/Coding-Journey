import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

# Shuffle the key for encryption/decryption
random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]
    else:
        cipher_text += letter

print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT (Type your own cipher text here)
print("\n--- Decryption Phase ---")
user_cipher = input("Enter a message to decrypt: ")
plain_text_recovered = ""

for letter in user_cipher:
    if letter in key:
        index = key.index(letter)
        plain_text_recovered += chars[index]
    else:
        plain_text_recovered += letter

print(f"Recovered original message: {plain_text_recovered}")
