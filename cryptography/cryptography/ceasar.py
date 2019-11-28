def encrypt(mess, key):
    res = ''
    for i in mess:
        res = res + chr((ord(i)+key - 97) % 26 + 97)
    return res


def decrypt(cipher, key):
    res = ''
    for i in cipher:
        res = res + chr((ord(i)-key - 97) % 26 + 97)
    return res


mess = 'Abcfdbxs'.lower()
cipher = encrypt(mess, 3)
print(cipher)
mess = decrypt(cipher, 3)
print(mess)
