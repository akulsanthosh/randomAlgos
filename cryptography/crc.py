def xor(data, key):
    n = len(data)
    res = ''
    for i in range(1, n):
        if(data[i] == key[i]):
            res = res + '0'
        else:
            res = res + '1'
    return res


def mod(data, key):
    n = len(key)
    data_t = data[0:n]
    while n < len(data):
        if data_t[0] == '1':
            data_t = xor(data_t, key) + data[n]
        else:
            data_t = xor(data_t, '0'*n) + data[n]
        n = n + 1
    if data_t[0] == '1':
        data_t = xor(data_t, key)
    else:
        data_t = xor(data_t, '0'*n)
    return data_t


key = "1101"
data = "100100"
data_new = data + '0'*(len(key) - 1)
rem = mod(data_new, key)
codeword = data + rem
rem = mod(codeword, key)
print(rem)
