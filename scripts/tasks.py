import time
from celery import Celery

# Define module
app = Celery("tasks",
             backend="redis://localhost:6379/0",
             broker="redis://localhost:6379/0",
             )


@app.task(name="tasks.add")
def add(x, y):
    """
    The decorator includes the app context and refers to the task method of app
    This function gets converted into a celery task via the decorator
    """
    total = x + y
    print("{} + {} = {}".format(x, y, total))
    time.sleep(10)
    return total

