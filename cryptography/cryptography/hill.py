import numpy as np


def encrypth(msg, key):
    keyarr = [(ord(x)-97) % 26 for x in key]
    msgarr = [(ord(x)-97) % 26 for x in msg]
    k = np.array(keyarr).reshape(len(msg), int(len(key)/len(msg)))
    m = np.array(msgarr).reshape(len(msg), 1)
    print(k)
    print(m)
    c = np.matmul(k, m)
    c = np.remainder(c, 26)
    c = c.reshape(1, len(msg))
    d = np.linalg.inv(k)
    cipher = [chr(i.tolist()) for i in np.nditer(c)]
    print(cipher)


key = "GYBNQKURP".lower()
msg = "ACT".lower()
encrypth(msg, key)
