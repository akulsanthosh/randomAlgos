def encrypth(msg, key):
    cipher = ''
    for i in range(len(msg)):
        cipher += chr((ord(msg[i])-97 + ord(key[i % len(key)])-97) % 26 + 97)
    return cipher


def decrypth(msg, key):
    plaintext = ''
    for i in range(len(msg)):
        plaintext += chr((ord(msg[i])-97 -
                          (ord(key[i % len(key)])-97) + 26) % 26 + 97)
    return plaintext


key = "AYUSH".lower()
msg = "GEEKSFORGEEKS".lower()
cipher = encrypth(msg, key)
print(cipher)
plaintext = decrypth(cipher, key)
print(plaintext)
