def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    shift, n = 0, len(keyword)
    for i in range(len(plaintext)):
        if ord("a") <= ord(keyword[i % n]) <= ord("z"):
            shift = ord(keyword[i % n]) - ord("a")
        else:
            shift = ord(keyword[i % n]) - ord("A")
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


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    shift, n = 0, len(keyword)
    for i in range(len(ciphertext)):
        if ord("a") <= ord(keyword[i % n]) <= ord("z"):
            shift = ord(keyword[i % n]) - ord("a")
        else:
            shift = ord(keyword[i % n]) - ord("A")
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
