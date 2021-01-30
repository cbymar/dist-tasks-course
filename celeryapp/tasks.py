import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from celeryapp.celeryconfig import app


@app.task(name='tasks.add')
def add(x, y):
    total = x + y
    print('{} + {} = {}'.format(x, y, total))
    time.sleep(2)
    return total


