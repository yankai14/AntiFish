from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()

@dataclass
class ENVIRONMENT_VARIABLES:
    TELEGRAM_BOT_TOKEN:str = os.getenv("TELEGRAM_BOT_TOKEN")
    API_BASE_URL: str = os.getenv("API_BASE_URL")


ENV = ENVIRONMENT_VARIABLES()