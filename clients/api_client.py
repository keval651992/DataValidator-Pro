import os
import requests
from dotenv import load_dotenv

load_dotenv()


class APIClient:

    def __init__(self):
        self.base_url = os.getenv(
            "API_BASE_URL", "https://jasonplaceholder.typicode.com"
        )


    def get_user_by_id(self, user_id: int) -> dict:
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()