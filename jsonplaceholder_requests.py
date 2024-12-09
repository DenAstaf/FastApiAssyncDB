__all__ = (
    "get_users",
    "get_posts",
    "get_data_http",
)

import aiohttp
import logging
import asyncio

log = logging.getLogger(__name__)


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:
            return await response.json()


async def fetch_posts() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:
            return await response.json()


async def get_users() -> dict:
    log.info("Start getting information users")
    users = await fetch_users()
    log.info("Got information users")
    return users


async def get_posts() -> dict:
    log.info("Start getting information posts")
    posts = await fetch_posts()
    log.info("Got information posts")
    return posts


async def get_data_http() -> tuple:
    """
    Создает 2 задания на получение данных по http
    и возвращает результат.
    Содержит данные по юзерам и постам.
    """

    log.info("Start get_data_http")

    # Создает группу заданий и выполняет ее
    async with asyncio.TaskGroup() as tg:
        task_users_get_data = tg.create_task(get_users())
        task_posts_get_data = tg.create_task(get_posts())

    # получает значение, которое возвращает функция
    users = task_users_get_data.result()
    posts = task_posts_get_data.result()

    log.info("Finish get_data_http")

    return users, posts
