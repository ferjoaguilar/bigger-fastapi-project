from bcrypt import hashpw, gensalt

def hash_password(password: str) -> str:
    return hashpw(password.encode(encoding='utf-8'), gensalt()).decode(encoding='utf-8')
    