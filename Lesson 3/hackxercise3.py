import itertools

all_ascii_chars = "".join([chr(i) for i in range(128)])

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r


def crack(s):
    s_len = len(s)
    s_hash = simple_hash(s)
    for l in range(s_len + 1):
        for string in itertools.imap(''.join, itertools.product(all_ascii_chars, repeat=l)):
            if simple_hash(string) == s_hash and string != s:
                return string
    return False
