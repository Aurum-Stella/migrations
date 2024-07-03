from config.aws_settings import AwsSettings
from dotenv import load_dotenv
import os
from urllib.parse import quote


class Settings:
    def __init__(self):
        load_dotenv()
        self.DB_HOST = os.getenv('DWH_HOST')
        self.DB_DB_NAME = os.getenv('DWH_DB_NAME')
        self.DB_USER = os.getenv('DWH_USER')
        self.DB_PASSWORD = AwsSettings.get_storage_password('DWH_PASSWORD')
        self.DB_PORT = os.getenv('DWH_PORT')

        if None in [self.DB_HOST, self.DB_DB_NAME, self.DB_USER, self.DB_PASSWORD, self.DB_PORT]:
            raise ValueError("Some required environment variables are missing")

    def database_connect(self):
        return (
            f"host={self.DB_HOST}"
            f"dbname={self.DB_DB_NAME}"
            f"user={self.DB_USER}"
            f"password={quote(self.DB_PASSWORD)}"
            f"port={self.DB_PORT}"
        )

    @property
    def test_url(self) -> str:
        return str("postgresql+psycopg://postgres:root@localhost:5432/postgres")

    @property
    def database_url(self) -> str:
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DB_NAME}"


settings = Settings()
