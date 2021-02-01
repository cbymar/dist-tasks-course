import os
import sys
from celery import Celery
from celery.schedules import crontab

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Define module
app = Celery("tasks",
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             task_serializer='json',
             result_serializer='json',
             accept_content=['json'],
             enable_utc=True,
             include=["celeryapp.tasks"]
             )

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'tasks.add': {
        'task': "tasks.add",
        'schedule': 5.0,
        'args': (2, 4)
    },
    'tasks.send_mail_from_queue': {
        'task': "tasks.send_mail_from_queue",
        'schedule': crontab(minute="*/1")
    },
}

if __name__ == "__main__":
    pass
