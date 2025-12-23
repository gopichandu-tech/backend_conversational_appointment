import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

CALENDLY_URL = os.getenv("CALENDLY_URL")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "")

ALLOWED_ORIGINS = [origin.strip() for origin in CORS_ORIGINS.split(",") if origin.strip()]
