import time
import sys
import os
import redis

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from celeryapp.celeryconfig import app


@app.task(bind=True, name='tasks.add')
def add(self, x, y):
    total = x + y
    print('{} + {} = {}'.format(x, y, total))
    time.sleep(2)
    return total

key = "4088587A2CAB44FD902D6D5C98CD2B17"

@app.task(bind=True, name='tasks.send_mail_from_queue')
def send_mail_from_queue(self):
    """Added redis locking mechanism """
    REDIS_CLIENT = redis.Redis()
    timeout = 60 * 5 # 5 minutes
    have_lock = False # initialize
    my_lock = REDIS_CLIENT.lock(key, timeout=timeout) # create the lock
    try:
        have_lock = my_lock.acquire(blocking=False)
        if have_lock:
            messages_sent = "Example.email"
            print("{} Email sent, [{}]".format(self.request.hostname, messages_sent))
            time.sleep(10) # example wait time to simulate long-running task
    finally:
        print("release lock at end")
        if have_lock:
            my_lock.release()
