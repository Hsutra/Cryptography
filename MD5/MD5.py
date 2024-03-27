import hashlib

def calculate_md5(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

# Пример использования
text = input("Введите текст для вычисления MD5: ")
md5_digest = calculate_md5(text)
print("MD5 хэш для введенного текста:", md5_digest)
