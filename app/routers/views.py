from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from models.db_async import async_session
from models.users import User
from jsonplaceholder_requests import get_data_http

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix='', tags=['Получение информации о всех пользователях'])


@router.get("/", response_class=HTMLResponse)
async def show_users(request: Request):
    """Отображает все данные из таблицы users на страничке"""
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        context = {
            "request": request,
            "users": users
        }
        return templates.TemplateResponse("index.html", context)


@router.post(
    "/add",
    response_class=HTMLResponse,
    summary="Добавление новой записи",
    description="""Добавляет новую запись""",
)
async def insert_users(request: Request, name: str = Form(...), username: str = Form(...), email: str = Form(...)):
    """Создает сессию, добавляет данные полученные из формы в БД таблицу users
    и отображает все данные из таблицы users на страничке"""
    async with async_session() as session:
        try:
            async with session.begin():
                new_user = User(name=name, username=username, email=email)
                session.add(new_user)

            await session.commit()

            message = "Запись успешно добавлена!"
        except IntegrityError:
            await session.rollback()  # Откатывает изменения
            return HTMLResponse(content="<p>Пользователь с такими данными уже существует.</p>", status_code=400)

        result = await session.execute(select(User))
        users = result.scalars().all()
        context = {
            "request": request,
            "users": users,
            "message": message,
        }
        return templates.TemplateResponse("index.html", context)


@router.post(
    "/add-all-user",
    response_class=HTMLResponse,
    summary="Добавление юзеров по HTTP",
    description="""Добавляет всех юзеров по HTTP""",
)
async def add_all_user(request: Request):
    """Создает сессию, добавляет все полученные данные по http в БД таблицу users
    и отображает их на страничке"""
    data_user = await get_data_http()
    async with async_session() as session:
        try:
            async with session.begin():
                for user in data_user[0]:
                    new_user = User(name=user["name"], username=user["username"], email=user["email"])
                    session.add(new_user)

            await session.commit()

            message = "Записи успешно добавлены!"
        except IntegrityError:
            await session.rollback()  # Откатывает изменения
            return HTMLResponse(content="<p>Пользователи с такими данными уже существуют.</p>", status_code=400)

        result = await session.execute(select(User))
        users = result.scalars().all()
        context = {
            "request": request,
            "users": users,
            "message": message,
        }
        return templates.TemplateResponse("index.html", context)
