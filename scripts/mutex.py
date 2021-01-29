import threading
import sys

args = sys.argv

counter_buffer = 0
counter_lock = threading.Lock()

COUNTER_MAX = int(args[1])
print(COUNTER_MAX)
# COUNTER_MAX = 100000

def consumer_1_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        # counter_lock.acquire()
        counter_buffer += 1
        # counter_lock.release()


def consumer_2_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        # counter_lock.acquire()
        counter_buffer += 1
        # counter_lock.release()

# initialize into individual threads
t1 = threading.Thread(target=consumer_1_counter())
t2 = threading.Thread(target=consumer_2_counter())

t1.start()
t2.start()

# Add to the main thread
t1.join()
t2.join()

print(counter_buffer)
