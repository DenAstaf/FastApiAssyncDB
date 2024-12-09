from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.views import router


# Создает экземпляр класса FastAPI
app = FastAPI()
# Подключает роутеры
app.include_router(router)
# Подключает static(js, css)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
