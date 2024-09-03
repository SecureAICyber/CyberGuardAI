import time
from collections import defaultdict
from src.cyberguardai.cryptography_service import CryptographyService
from src.cyberguardai.database_service import DatabaseService
from src.cyberguardai.logging_service import LoggingService

class AuthenticationService:
    def __init__(self, db_service: DatabaseService, crypto_service: CryptographyService, logging_service: LoggingService):
        self.db_service = db_service
        self.crypto_service = crypto_service
        self.logging_service = logging_service
        self.login_attempts = defaultdict(int)
        self.last_login_attempt = defaultdict(int)

    def register_user(self, username, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        hashed_password = self.crypto_service.hash_password(password)
        self.db_service.save_user(username, hashed_password)

    def authenticate_user(self, username, password):
        current_time = time.time()
        if self.login_attempts[username] >= 3 and current_time - self.last_login_attempt[username] < 60:
            self.logging_service.log_info("Too many login attempts, please wait and try again.")
            return False

        hashed_password = self.db_service.get_hashed_password(username)
        if not hashed_password:
            return False

        if self.crypto_service.verify_password(password, hashed_password):
            self.login_attempts[username] = 0
            return True
        else:
            self.login_attempts[username] += 1
            self.last_login_attempt[username] = current_time
            return False
