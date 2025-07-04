FROM python:3.10-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
CMD ["celery", "-A", "src.celery_worker.celery_worker", "worker", "--loglevel=info"]