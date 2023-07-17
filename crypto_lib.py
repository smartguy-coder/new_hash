import hashlib

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def encode_md5(value: str) -> str:
    result = hashlib.md5(value.encode()).hexdigest()
    return result


def get_password_hash(password: str) -> str:
    result = pwd_context.hash(password)
    return result


def verify_password(plain_password: str, hashed_password: str) -> bool:
    result = pwd_context.verify(plain_password, hashed_password)
    return result
