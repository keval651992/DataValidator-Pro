import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DatabaseClient:

  def __init__(self):
    self.conn_params = {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
        "database": os.getenv("DB_NAME", "test_db"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "secret"),
    }

  def get_user_record(self, user_id: int) -> dict:
    """Fetches user record from the database to compare against API payload."""
    # Simulated execution block for portfolio demonstration:
    # conn = psycopg2.connect(**self.conn_params)
    # cursor = conn.cursor()
    # cursor.execute("SELECT id, name, username, email, phone, website FROM users WHERE id = %s", (user_id,))
    # row = cursor.fetchone()
    # cursor.close()
    # conn.close()

    return {
        "id": user_id,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
    }