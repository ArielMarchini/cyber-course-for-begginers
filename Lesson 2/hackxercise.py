from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english

K_MAX_POSSIBLE_VALUE = "999999"
K_MIN_POSSIBLE_VALUE = "0360000000000000"

def brute_force_aes(ciphertext):
    print(aes_decrypt(ciphertext))
