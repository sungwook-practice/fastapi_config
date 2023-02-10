from fastapi import Depends, FastAPI

from config import Settings, loadSetting

app = FastAPI()


def get_settings() -> Settings:
    return loadSetting()()


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }