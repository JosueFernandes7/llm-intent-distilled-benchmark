import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]

settings = Settings()