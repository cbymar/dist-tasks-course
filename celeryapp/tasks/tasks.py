import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from celeryapp.celeryconfig import app


@app.task(name='tasks.add')
def add(x, y):
    total = x + y
    print('{} + {} = {}'.format(x, y, total))
    time.sleep(2)
    return total


@app.task(name='tasks.send_mail_from_queue')
def send_mail_from_queue():
    try:
        messages_sent = "Example.email"
        print("Email sent, [{}]".format(messages_sent))
    finally:
        print("release resources at end")
