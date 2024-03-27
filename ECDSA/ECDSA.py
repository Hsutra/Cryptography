from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import os


def generate_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def sign_file(private_key, file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    signature = private_key.sign(
        file_data,
        ec.ECDSA(hashes.SHA256())
    )
    return signature


def verify_signature(public_key, file_path, signature):
    with open(file_path, "rb") as file:
        file_data = file.read()

    try:
        public_key.verify(
            signature,
            file_data,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception as e:
        print("Verification failed:", e)
        return False


# Пример использования
private_key, public_key = generate_keypair()

file_path = "example.txt"
file_data = b"This is an example file."

# Сохраняем данные в файл
with open(file_path, "wb") as file:
    file.write(file_data)

# Подписываем файл
signature = sign_file(private_key, file_path)

# Проверяем подпись
if verify_signature(public_key, file_path, signature):
    print("Signature verified successfully.")
else:
    print("Signature verification failed.")
