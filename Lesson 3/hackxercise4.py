import hashlib
import itertools


ALL_ASCII_CHARS = "".join([chr(i) for i in range(128)])


def weak_md5(s):
    return hashlib.md5(s).hexdigest()[:5]


def find_collisions():
    hash_results = {}
    length = 0
    while True:
        for value in itertools.imap(''.join, itertools.product(ALL_ASCII_CHARS, repeat=length)):
            key = weak_md5(value)
            if key in hash_results:
                return (value, hash_results[key])
            hash_results[key] = value
        length += 1
