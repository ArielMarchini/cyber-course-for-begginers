def generateKey(string, codeword):
    codeword = list(codeword)
    if len(string) == len(codeword):
        return(codeword)
    else:
        for i in range(len(string) -
                       len(codeword)):
            codeword.append(codeword[i % len(codeword)])
    return("" . join(codeword))


def vigenere_encrypt(plaintext, codeword):
    key = generateKey(plaintext, codeword)
    cipher_text = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
