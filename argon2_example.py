from pyargon2 import hash

password = 'a strong password'
salt = 'a unique salt'
hex_encoded_hash = hash(password, salt)
print(hex_encoded_hash)


def hashing_password(password):
    """Функция хэширующая пароли по алгоритму Argon2"""
    salt = "SLAVIK&VOVAN_DEV"
    return hash(password, salt)


print(type(hashing_password("Vasya")))
