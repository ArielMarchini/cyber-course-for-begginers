def get_prg(plaintext_size, k):
    new_k = []
    k = list(k)
    i = j = 0
    for x in range(plaintext_size):
        i = (i + 1) % 32
        j = (j + ord(k[i])) % 32
        k[i], k[j] = k[j], k[i]  # swap
        new_k.append(k[(k[i] + k[j]) % 32])

def fake_rc4(plaintext, keystream):
    pass # return ciphertext



get_prg(32, "abcdeabcdeabcdeabcdeabcdeabcde12")
