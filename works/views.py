import random
import time

from django.http import HttpResponse

from works.models import Work


def f(n):
    return 1 if n <= 1 else f(n-1) + f(n-2)


def process_work(request):
    tick = time.time()
    n = random.randrange(35, 42)

    Work(
        n=n,
        result=f(n),
        elapsed_time=str(time.time() - tick),
    ).save()

    return HttpResponse('done')
