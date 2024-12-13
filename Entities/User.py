import hashlib

class User:
    def __init__(self, email, password):
        self.email = email
        self.hashed_password = self._hash_password(password) if password else None

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
