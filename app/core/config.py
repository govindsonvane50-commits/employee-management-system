import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Employee Management System API"
    PROJECT_VERSION: str = "1.0.0"

    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "employee_management_db")

    @property
    def DATABASE_URL(self) -> str:
        encoded_password = urllib.parse.quote_plus(self.DB_PASSWORD)
        return f"mysql+pymysql://{self.DB_USER}:{encoded_password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
