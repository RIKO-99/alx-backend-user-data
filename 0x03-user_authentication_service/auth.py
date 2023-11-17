"""_import libraries
"""
import bcrypt

def _hash_password(password: str) -> bytes:
        """_summary_

    Returns:
        str: hashed passwd
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
