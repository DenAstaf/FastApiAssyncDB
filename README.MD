В данном процессе реализована через асинхронн работа с БД (Postgre) и отображение данных через FastApi (ASGI-сервер - Uvicorn).
<br>Так же через форму можно добавлять пользователей в БД (стоит валидация на дубликаты пользователей, username и email должны быть уникальными).
<br>Так же реализовано получение массово данных через aiohttp и загрузка их в БД.

Для запуска проекта необходимо:

1. Установить Poetry: pip install poetry
3. Выполните команду, чтобы создать миграцию (в приложенном проекте миграция уже сделана): `docker-compose run app alembic revision --autogenerate -m "migration"`
4. Выполнить команду, чтобы применить миграцию: `docker-compose run app alembic upgrade head`
5. Выполнить команду, чтобы запустить сервисы: `docker-compose up -d --build`
6. Перейти по ссылке: http://127.0.0.1:8000/, там будут отображены данные с таблицы "users", а так же форма для добавления новых данных в таблицу "users".

<br>P.S. В проекте есть, но не используется таблица "posts". Между таблицами "users" и "posts" настроено отношение "один ко многим", где один пользователь может быть связан с несколькими постами, но каждый пост может ссылаться только на одного пользователя.
Полная работа данного функционала с получением и заполнением данных в таблицы реализована в проекте - "assyncHttp-Db".
