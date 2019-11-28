def sortlist(msg, key):
    pair = zip(key, msg)
    temp = [x for _, x in sorted(pair)]
    return temp


def encrypth(msg, key):
    keyarr = [x for x in key]
    msgarr = []
    temp = []
    for i in msg:
        if len(temp) == len(keyarr):
            msgarr.append(sortlist(temp, keyarr))
            temp = []
        temp.append(i)
    msgarr.append(sortlist(temp, keyarr))
    cipher = ''
    for i in range(len(msgarr[0])):
        for j in range(len(msgarr)):
            cipher = cipher + msgarr[j][i]
    return cipher


def decrypth(msg, key):
    keyarr = [x for x in key]
    n = int(len(msg) / len(key))
    msgarr = [[] for x in range(n)]
    for i in range(len(msg)):
        msgarr[i % n].append(msg[i])
    final = []
    for i in msgarr:
        final.append(sortlist(i, key))
    plaintext = ''
    for i in final:
        for j in i:
            plaintext = plaintext + j
    return plaintext


key = "dcba"
mes = "hello world i am akul"
mes = mes + " "*(len(key) - (len(mes) % len(key)))
ciphertext = encrypth(mes, key)
print(ciphertext)
plaintext = decrypth(ciphertext, key)
print(plaintext)
