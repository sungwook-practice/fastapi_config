from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Default app_name"
    admin_email: str = "default@email.com"
    items_per_user: int = 50

    class Config:
        env_file = ".env"
