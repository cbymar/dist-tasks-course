import os
import sys
from celery import Celery
from celery.schedules import crontab

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


# Define module
app = Celery("tasks",
             backend="redis://localhost:6379/0",
             broker="redis://localhost:6379/0",
             include=["celeryapp.tasks.tasks"]
             )

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'tasks.add': {
        'task': "tasks.add",
        'schedule': 5.0,
        'args': (2, 4)
    },
    'tasks.add': {
        'task': "tasks.send_mail_from_queue",
        'schedule': crontab(minute="*/1")
    },
}

# app.conf.beat_schedule = {
#     'tasks.add': {
#         'task': "tasks.send_mail_from_queue",
#         'schedule': 5.0
#     },
# }


app.start()
if __name__ == "__main__":
    pass
