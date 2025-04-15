from app.tasks.scheduler import celery_app
from celery.beat import PersistentScheduler

if __name__ == "__main__":
    celery_app.start(argv=["celery", "beat", "-S", "celery.beat:PersistentScheduler", "-l", "info"])