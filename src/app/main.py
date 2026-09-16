from importlib.metadata import metadata
from typing import Annotated

from fastapi import Depends, FastAPI

from app.config.settings import Settings, get_settings

app_settings = get_settings()

project_metadata = metadata("DevBrain")
app_name = project_metadata["Name"]
app_version = project_metadata["Version"]
app_description = project_metadata["Summary"]
app = FastAPI(
    title=app_name,
    version=app_version,
    description=app_description,
    docs_url=None if app_settings.is_prod_env else "/docs",
    redoc_url=None if app_settings.is_prod_env else "/redoc",
)


@app.get("/")
def root(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "service": app_name,
        "version": app_version,
        "environment": settings.app_env,
        "status": "ok",
    }


@app.get("/health")
def health():
    return {"status": "ok"}
