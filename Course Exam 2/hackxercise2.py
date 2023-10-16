import random
import hashlib
import os
from Crypto.Cipher import AES

# you can use the imports, and you can solve with your own imports

p = 283
g = 47


class SecureChannel:

    def __init__(self, p, g):
        self.a = random.randint(1, p)

    def publish(self):
        return pow(g, self.a) % p

    def encrypt(self, gb, text):
        s = str(pow(gb, self.a) % p)
        iv = "asdfghjklzxcvbnm"
        hash = hashlib.sha256(s.encode()).hexdigest()[:16]
        c = AES.new(hash, AES.MODE_CBC, iv)
        return c

