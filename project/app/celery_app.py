import os
from celery import Celery

redisHost = os.getenv("REDIS_HOST", "redis")
redisPort = int(os.getenv("REDIS_PORT", 6379))

celeryApp = Celery(
    "app",
    broker=f"redis://{redisHost}:{redisPort}/0",
    backend=f"redis://{redisHost}:{redisPort}/1",
)

celeryApp.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)

@celeryApp.task
def ping():
    return "pong"