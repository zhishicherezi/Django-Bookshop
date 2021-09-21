import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj', broker='redis://localhost:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Выполняется каждые 15 минут
    "creating_random_book":{
        'task': "books.tasks.random_book_add",
        'schedule': crontab(minute='*/15'),
        },
        # ежедневно в 15:22
    "updating_author_list":{
        'task': 'books.tasks.author_add',
        'schedule': crontab(hour=15, minute=22),
        },
    # рассылка во вт.,пт. в 19:00
    "email_notification":{
        'task': 'books.tasks.send_mail_book_created',
        'schedule': crontab(
            minute=0, 
            hour=19,
            day_of_week='thu,fri'),
        },
}

