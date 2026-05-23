from passlib.context import CryptContext
import hashlib

context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    to_encode = password.encode("utf-8")
    sha = hashlib.sha256(to_encode).hexdigest()
    hashed = context.hash(sha)
    return hashed

def verify_pass(plain: str, hash_pass: str) -> bool:
    to_encode = plain.encode("utf-8")
    sha = hashlib.sha256(to_encode).hexdigest()
    result = context.verify(sha, hash_pass)
    return result