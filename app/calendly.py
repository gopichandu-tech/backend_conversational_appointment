from app.config import CALENDLY_URL
from urllib.parse import urlencode

def create_calendly_booking(user_data):
    if not CALENDLY_URL:
        raise ValueError("CALENDLY_URL is not set")

    params = {
        "name": user_data.get("name", ""),
        "email": user_data.get("email", "")
    }

    return f"{CALENDLY_URL}?{urlencode(params)}"
