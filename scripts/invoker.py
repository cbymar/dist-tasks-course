from tasks import add

"""
Add is a task in celery, per the decorator
So it gets a few additional methods
"""

add.delay(1, 2)
