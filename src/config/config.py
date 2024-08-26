import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class AppConfig:
    APP_NAME = os.getenv("APP_NAME", "enbdleap-python-core")
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = int(os.getenv("APP_PORT", 8000))
    APP_DEBUG = os.getenv("APP_DEBUG", "False").lower() in ["true", "1", "yes"]
