from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env from project root no matter where pytest is run from
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=ENV_PATH)

class Settings:
    BASE_URL = os.getenv("BASE_URL")
    TIMEOUT = int(os.getenv("TIMEOUT_SECONDS", "10"))

    def validate(self):
        if not self.BASE_URL:
            raise ValueError(f"BASE_URL is missing. Check {ENV_PATH}")

settings = Settings()
settings.validate()