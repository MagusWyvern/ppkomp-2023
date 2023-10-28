'''
Cryptography (from Ancient Greek: κρυπτός, romanized: kryptós "hidden, secret"; and γράφειν graphein, "to write"), is the process of hiding information so that only the sender and receiver of the message can read it.

Encryption is the process of hiding the plaintext by converting the plaintext into cipher text.
Decryption is the process of translating the ciphertext back into the plaintext.

In cryptography, a substitution cipher is a method of encrypting in which units of plaintext are replaced with the ciphertext, with the help of a key. The receiver deciphers the text by performing the inverse substitution process to extract the original message.

In the Caesar Cipher, each letter in the alphabet was mapped to a different letter.

Example 1: A→B, B→C, C→D, ..., Z→A when we're using key = 1.
Example 2: A→D, B→E, C→F, ..., Z→C when we're using key = 3
Example 3: A→I, B→J, C→K, ..., Z→H when we're using key = 8

Given the key used for the encryption and plaintext, you are to convert that plaintext into ciphertext.
'''

key = int(input())
plaintext = input()

ciphertext = ''
normal_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create the shifted alphabet

shifted_alphabet = ''

for i in range(len(normal_alphabet)):
    shifted_alphabet += normal_alphabet[(i + key) % 26]

# Convert each letter in the plaintext into ciphertext
# If the letter is not an alphabet, leave it as it is
# Watch for upper case v.s lower case characters
# Use the shifted alphabet to convert the plaintext into ciphertext

for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        if plaintext[i].isupper():
            ciphertext += shifted_alphabet[normal_alphabet.index(plaintext[i])]
        elif plaintext[i].islower():
            ciphertext += shifted_alphabet[normal_alphabet.index(plaintext[i].upper())].lower()
    else:
        ciphertext += plaintext[i]

print(ciphertext)