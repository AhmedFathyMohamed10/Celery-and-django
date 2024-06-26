from celery import shared_task
from time import sleep

@shared_task
def wake_up(time_to_set):
    sleep(time_to_set)
    return None