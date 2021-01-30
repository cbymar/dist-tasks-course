import os
import sys
from celery import Celery


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


# Define module
app = Celery("tasks",
             backend="redis://localhost:6379/0",
             broker="redis://localhost:6379/0",
             include=["celeryapp.tasks"]
             )


app.conf.beat_schedule = {
    'tasks.add': {
        'task': "tasks.add",
        'schedule': 5.0,
        'args': (2, 4)
    },
}
app.conf.timezone = 'UTC'

if __name__ == "__main__":
    app.start()
