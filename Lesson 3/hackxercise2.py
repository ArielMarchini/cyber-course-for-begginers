MUL_VALUE = 31
START_VALUE = 7
MODULO_VALUE = pow(2, 16)

def simple_hash(s):
    r = START_VALUE
    for c in s:
        r = r * MUL_VALUE
        r = r + ord(c)
        r = r % MODULO_VALUE
    return r
