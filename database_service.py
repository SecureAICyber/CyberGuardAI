import sqlite3
import time

class DatabaseService:
    def __init__(self, logging_service):
        self.logging_service = logging_service
        self.connect_to_database()

    def connect_to_database(self):
        try:
            self.conn = sqlite3.connect('users.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                (username text, password_hash text)''')
        except sqlite3.Error as e:
            self.logging_service.log_error("Database connection failed: " + str(e))
            time.sleep(5)
            self.connect_to_database()  # Retry after 5 seconds

    def save_user(self, username, hashed_password):
        try:
            self.cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
            self.conn.commit()
        except sqlite3.Error as e:
            self.logging_service.log_error("User saving failed: " + str(e))

    def get_hashed_password(self, username):
        try:
            self.cursor.execute("SELECT password_hash FROM users WHERE username=?", (username,))
            result = self.cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            self.logging_service.log_error("Fetching hashed password failed: " + str(e))
            return None
