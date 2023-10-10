from collections import Counter

MOST_FREQUENT_LETTERS = ['e', 't', 'a', 'o', 'i', 'n']
COUNT = 3

def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def is_english(s):
    try:
        s = s.lower()
        if is_ascii(s):
            for i in range(COUNT):
                if s == '':
                    return False
                most_common_char = Counter(s).most_common(1)[0][0]
                if not most_common_char in MOST_FREQUENT_LETTERS:
                    return False
                s = s.replace(most_common_char, '')
            return True
        return False
    except:
        return False
