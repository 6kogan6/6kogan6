import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        a = ord(plaintext[i]) + shift
        if ord("a") <= ord(plaintext[i]) <= ord("z"):
            if a > ord("z"):
                ciphertext += chr(a - 26)
            else:
                ciphertext += chr(a)
        elif ord("A") <= ord(plaintext[i]) <= ord("Z"):
            if a > ord("Z"):
                ciphertext += chr(a - 26)
            else:
                ciphertext += chr(a)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        a = ord(ciphertext[i]) - shift
        if ord("a") <= ord(ciphertext[i]) <= ord("z"):
            if a < ord("a"):
                plaintext += chr(a + 26)
            else:
                plaintext += chr(a)
        elif ord("A") <= ord(ciphertext[i]) <= ord("Z"):
            if a < ord("A"):
                plaintext += chr(a + 26)
            else:
                plaintext += chr(a)
        else:
            plaintext += ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
