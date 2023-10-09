alphabet = "abcdefghijklmnopqrstuvwxyz"
K_MAX_VALUE = 25
K_MIN_VALUE = 0

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    """Print all the results from the brute force"""
    for k in range(K_MIN_VALUE, K_MAX_VALUE + 1):
        print(decrypt(ciphertext, k))
        
    """The right value of k"""
    print("-------------------------------------------")
    k_right_value = 17
    print("The plaintext is:")
    print(decrypt(ciphertext, k_right_value))
    print("The right k value is:")
    print(k_right_value)
    print("-------------------------------------------")
    return k_right_value
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
