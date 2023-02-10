from fastapi import Depends, FastAPI

from config import Settings

app = FastAPI()


def get_settings() -> Settings:
    return Settings()


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    print(settings)
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }