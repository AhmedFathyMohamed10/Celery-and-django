from django.http import HttpResponse
from .tasks import wake_up

def index(request): 
    wake_up.delay(5)
    return HttpResponse("I'm about to wake up now...")