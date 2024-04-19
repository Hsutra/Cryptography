import random
import math

def coprime(m):
    elist = [i for i in range(2, m) if math.gcd(m, i) == 1]
    return random.choice(elist)

def generate_private_key(n):
    private_key = [random.randint(1, 10)]
    for i in range(1, n):
        next_value = random.randint(sum(private_key) + 1, sum(private_key) + 10)
        private_key.append(next_value)
    m = random.randint(sum(private_key) + 1, sum(private_key) + 10)
    e = coprime(m)
    return private_key, m, e

def generate_public_key(private_key, m, e):
    return [(elem * e) % m for elem in private_key]

def split_string(string, chunk_size):
    return [string[i: i+chunk_size] for i in range(0, len(string), chunk_size)]

def encrypt(plaintext, public_key):
    binary_representation = ''.join(format(ord(char), '08b') for char in plaintext)
    binary_representation = split_string(binary_representation, len(public_key))
    #print(binary_representation)
    encrypted_text = []
    for i in binary_representation:
        sum = 0
        count = 0
        for j in i:
            if j == '1':
               sum += public_key[count]
            count += 1
        encrypted_text.append(sum)
    return encrypted_text

def binary_to_text(binary_representation):
    text = ''
    for i in range(0, len(binary_representation), 8):
        byte = binary_representation[i: i+8]  # Получаем байт из бинарного представления
        char = chr(int(byte, 2))  # Преобразуем байт в символ
        text += char
    return text[:-1]

def decrypt(encrypted_text, private_key, m, e):
    u = [i for i in range(m - 1) if (e * i) % m == 1][0]
    res = [(elem * u) % m for elem in encrypted_text]
    bin_list = []
    for j in range(len(res)):
        sequence = [0] * len(private_key)
        for i, num in enumerate(private_key[::-1]):
            if res[j] >= num:
                sequence[len(private_key) - i - 1] = 1
                res[j] -= num
                if res[j] == 0:
                    break
        bin_list.append(sequence)
    merged_sequence = []
    for sublist in bin_list:
        merged_sequence.extend(sublist)
    bin_text = ''.join(str(bit) for bit in merged_sequence)
    return binary_to_text(bin_text)


n = 6
private_key, m, e = generate_private_key(n)
public_key = generate_public_key(private_key, m, e)
plaintext = "Hello, World!"
encrypted_text = encrypt(plaintext, public_key)
decrypted_text = decrypt(encrypted_text, private_key, m, e)
print(decrypted_text)
