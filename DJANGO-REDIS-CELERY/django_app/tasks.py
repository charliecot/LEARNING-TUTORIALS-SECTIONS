from celery import shared_task
 

# Simple async task
@shared_task
def add(x, y):
    return x + y