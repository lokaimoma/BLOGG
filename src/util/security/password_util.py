from . import pwd_context


def hash_password(password: str) -> str:
    """
        A helper function for hashing
        passwords.

        Args
        ----
        password: str

        Returns
        -------
        hashed password:str
    """
    return pwd_context.hash(secret=password)


def verify_password_hash(password: str, password_hash: str) -> bool:
    """
        Helper function for verifying hashed password against
        plain password.

        Args
        ----
        password: str
        password_hash: str

        Returns
        -------
        bool (Confirming if password is same as the hashed version)
    """
    return pwd_context.verify(secret=password, hash=password_hash)
