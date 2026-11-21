# FastAPI App

## Публичный адрес
https://your-app.up.railway.app

## Документация
https://your-app.up.railway.app/docs

## Локальный запуск через Docker
docker compose up --build

## Проверка
- http://localhost:8000/ — корень
- http://localhost:8000/health — проверка Postgres + Redis
- http://localhost:8000/docs — Swagger UI

## Переменные окружения
Файл `.env.docker` — хосты `db` и `redis` (имена сервисов Docker-сети).