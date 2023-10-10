# from Crypto.Cipher import AES
# from Crypto import Random

IV = "arielistheking11"
IV_ASCII = [ord(c) for c in IV]
BLOCK_SIZE_IB_BYTES = 16


def xor_lists(l1, l2):
    return list(a^b for a,b in zip(l1, l2))


def get_block_from_text_ascii(text_ascii, index_block):
    start_byte = (index_block - 1) * BLOCK_SIZE_IB_BYTES
    end_byte = index_block * BLOCK_SIZE_IB_BYTES
    return text_ascii[start_byte: end_byte]


def create_c_next(c_prev, k_ascii, m_ascii):
    return xor_lists(xor_lists(c_prev, m_ascii), k_ascii)


def aes_encrypt(plaintext, k):
    k_ascii = [ord(c) for c in k]
    plaintext_ascii = [ord(c) for c in plaintext]
    index_block = 1
    m1 = get_block_from_text_ascii(plaintext_ascii, index_block)
    c1 = xor_lists(xor_lists(m1, IV_ASCII), k_ascii)
    c_total = c1
    c_prev = c1
    while(index_block * BLOCK_SIZE_IB_BYTES < len(plaintext)):
        index_block = index_block + 1
        m_current = get_block_from_text_ascii(plaintext_ascii, index_block)
        c_current = create_c_next(c_prev, k_ascii, m_current)
        c_total.extend(c_current)
        c_prev = c_current
    return "".join([chr(c) for c in c_total])



def aes_decrypt(ciphertext, k):
    k_ascii = [ord(c) for c in k]
    ciphertext_ascii = [ord(c) for c in ciphertext]
    index_block = 1
    c1 = get_block_from_text_ascii(ciphertext_ascii, index_block)
    m1 = xor_lists(xor_lists(k_ascii, c1), IV_ASCII)
    m_total = m1
    c_prev = c1
    while(index_block * BLOCK_SIZE_IB_BYTES < len(ciphertext)):
        index_block = index_block + 1
        c_current = get_block_from_text_ascii(ciphertext_ascii, index_block)
        m_current = xor_lists(xor_lists(c_current, k_ascii), c_prev)
        m_total.extend(m_current)
    return "".join([chr(c) for c in m_total])
