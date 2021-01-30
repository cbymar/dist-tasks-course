import threading
import time
import random
import queue

thequeue = queue.Queue(10)
MAX_ITEMS = 10

class ProducerThread(threading.Thread):
    """
    Process that writes to the queue when appropriate
    """
    def run(self):
        """Get signal and write"""
        numbers = range(5)
        global thequeue
        while True:
            number = random.choice(numbers)
            thequeue.put(number)
            print("Produced {}".format(number))
            print("Queue size = {}".format(thequeue.qsize()))
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    """
    Process that removes from queue when appropriate
    """
    def run(self):
        """Get signal and consume"""
        global thequeue
        while True:
            number = thequeue.get()
            thequeue.task_done() # tell the queue we just extracted an item.
            print("Consumed {}".format(number))
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
