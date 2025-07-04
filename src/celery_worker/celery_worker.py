from celery import Celery

from src.config import celery_config

celery_app = Celery(
    'tasks', broker=celery_config.broker,
    backend=celery_config.backend
)

celery_app.conf.task_routes = {
    'src.celery_worker.task': {"queue": "balance_queue"}
}

celery_app.autodiscover_tasks(["src.celery_worker"])


if __name__ == "__main__":
    celery_app.worker_main(["worker", "--loglevel=info", "--pool=threads"])
