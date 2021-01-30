import threading
import time
import random

queue = []
MAX_ITEMS = 10




# condition var lets threads wait until notified by another thread
condition = threading.Condition()

class ProducerThread(threading.Thread):
    """

    """
    def run(self):

        numbers = range(5)
        global queue

        while True:
            condition.acquire()
            if len(queue) == MAX_ITEMS:
                print("Queue full and producer waiting")
                condition.wait() # waits for the consumer to act (releases lock to consumer)
                print("Space in queue, Consumer notified producer")
            number = random.choice(numbers)
            queue.append(number)
            print("Produced {}".format(number))
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    """
    Pop, notify, then release the lock to producer
    Or if wait() is called, auto-releases lock to producer (no notification needed)
    """
    def run(self):

        global queue

        while True:
            condition.acquire()
            if not queue:
                print("Nothing in queue, consumer is waiting")
                condition.wait() # blocks consumer & releases lock (upf grabs by producer)
                print("Producer added something to queue and notified consumers")
            number = queue.pop(0)
            print("Consumed {}".format(number))
            condition.notify() # tells producer but does not actually release lock back to producer
            condition.release() # this does.
            time.sleep(random.random())


producer = ProducerThread()
producer.daemon = True # these guys die when __main__ thread stops.
producer.start()

consumer = ConsumerThread()
consumer.daemon = True
consumer.start()

"""
If we allow the main thread to not end (until a keyboard interrupt), then 
they keyboard interrupt will interrupt the daemon threads
"""
while True:
    time.sleep(1)
