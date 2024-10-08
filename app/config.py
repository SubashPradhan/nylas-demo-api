import os
from dotenv import load_dotenv
load_dotenv()

class BaseConfig:
  HOST = "0.0.0.0"
  PORT = int(os.environ.get("PORT", 8000))
  NYLAS_CLIENT_ID = os.environ.get("NYLAS_CLIENT_ID")
  NYLAS_API_KEY = os.environ.get("NYLAS_API_KEY")
  NYLAS_REDIRECT_URI = "http://localhost:8000/nylas/callback"
  NYLAS_BASE_URL = "https://api.us.nylas.com/v3"
  JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
