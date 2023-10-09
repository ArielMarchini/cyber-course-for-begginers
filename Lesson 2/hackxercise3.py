def encrypt(plaintext, k):
    plaintext_ascii = [ord(c) for c in plaintext]
    k_ascii = [ord(c) for c in k]
    xor_chars_results = list(chr(a^b) for a,b in zip(plaintext_ascii,k_ascii))
    ciphertext ="".join([str(i) for i in xor_chars_results])
    return ciphertext
