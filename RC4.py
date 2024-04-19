def initialize_rc4(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def generate_keystream(S, length):
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream_byte = S[(S[i] + S[j]) % 256]
        keystream.append(keystream_byte)
    return keystream

def rc4_encrypt(plaintext, key):
    key = [ord(char) for char in key]
    S = initialize_rc4(key)
    keystream = generate_keystream(S, len(plaintext))
    ciphertext = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
    return ciphertext

def rc4_decrypt(ciphertext, key):
    return rc4_encrypt(ciphertext, key)  # RC4 decryption is the same as encryption

# Пример использования
plaintext = "вфы, world!"
key = "secretkey"

encrypted_text = rc4_encrypt(plaintext.encode(), key)
decrypted_text = rc4_decrypt(encrypted_text, key)

print("Original text:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text.decode())
