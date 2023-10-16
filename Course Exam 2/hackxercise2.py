import random
import hashlib
import os
from Crypto.Cipher import AES

# you can use the imports, and you can solve with your own imports

p = 283
g = 47


class SecureChannel:

    def __init__(self, p, g):
        self.a = random.randint(2, p - 1)

    def publish(self):
        return pow(g, self.a) % p

    def encrypt(self, gb, text):
        print(text)
        s = str(pow(gb, self.a) % p)
        s_hash = hashlib.sha256(s.encode()).hexdigest()[:16]
        iv = "gk5nsxxi98ql09jj"
        decipher = AES.new(s_hash, AES.MODE_CBC, iv)
        print(decipher)
        # print(iv + decipher)
        # return iv + decipher
        
s1 = SecureChannel(p, g)
s2 = SecureChannel(p, g)
s1.encrypt(s2.publish(), "1234567891234567")
