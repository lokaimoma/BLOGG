from passlib.context import CryptContext


pwd_context: CryptContext = CryptContext(
    schemes=["pbkdf2_sha256"], deprecated="auto")
