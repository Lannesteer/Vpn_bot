from src.database.keys.models import Key
from src.database.servers.models import Server
from src.database.users.models import User
from celery import Celery
from src.config import CeleryConfig

celery_app = Celery(
    'vpn_bot', broker=CeleryConfig.broker,
    backend=CeleryConfig.backend
)

celery_app.conf.task_routes = {
    'src.celery_worker.task': {"queue": "balance_queue"}
}

celery_app.autodiscover_tasks(["src.celery_worker.tasks"])


if __name__ == "__main__":
    celery_app.worker_main(["worker", "--loglevel=info", "--pool=prefork"])
