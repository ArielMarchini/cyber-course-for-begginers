import hashlib


HASH_LENGTH = 20


def sign(line: str):
    line = line.encode()
    hash = hashlib.sha1(line).hexdigest()
    desire_hash = hash[:HASH_LENGTH]
    return desire_hash


def scan(paths: list, signature: str):
    bad_paths = []
    for path in paths:
        f = open(path, "r")
        for line in f.readlines():
            signed_line = sign(line.strip())
            if signed_line == signature:
                bad_paths.append(path)
        f.close()
    return bad_paths

