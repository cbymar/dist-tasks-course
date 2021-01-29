from celery import Celery

# Define module
app = Celery("tasks", backend=None, broker="redis://localhost:6379/0")


@app.task(name="tasks.add")
def add(x, y):
    """
    The decorator includes the app context and refers to the task method of app
    This function gets converted into a celery task via the decorator
    """
    print("{} + {} = {}".format(x, y, x+y))
