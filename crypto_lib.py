import hashlib


def encode_md5(value: str) -> str:
    result = hashlib.md5(value.encode()).hexdigest()
    return result
