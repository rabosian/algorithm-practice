from hashlib import new


def caesarCipher(s, k):
    newList = list(s)
    for i in range(len(newList)):
        if ord(newList[i]) >= 65 and ord(newList[i]) <= 90:
            newList[i] = chr(65 + (ord(newList[i]) - 65 + k) % 26)
        elif ord(newList[i]) >= 97 and ord(newList[i]) <= 122:
            newList[i] = chr(97 + (ord(newList[i]) - 97 + k) % 26)
    return ''.join(newList)


s = 'middle-Outz'
print(caesarCipher(s, 2))