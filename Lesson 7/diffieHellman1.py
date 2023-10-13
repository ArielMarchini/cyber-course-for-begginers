P = 13
AMOUNT_OF_BASE_TO_FIND = 4


def is_good_base(p, g):
    numbers_presence = [False for i in range(p - 1)]
    for i in range(1, p):
        numbers_presence[(pow(g, i) % p) - 1] = True
    if False in numbers_presence: 
        return False
    return True


def find_base(p):
    possible_base = 0
    good_bases = []
    while len(good_bases) < AMOUNT_OF_BASE_TO_FIND:
        if is_good_base(p, possible_base):
            good_bases.append(possible_base)
        possible_base += 1
    return good_bases
