import time

from celery import shared_task

from works.models import Work


def f(n):
    return 1 if n <= 1 else f(n - 1) + f(n - 2)


@shared_task
def fibonacci(number):
    tick = time.time()

    work = Work.objects.create(n=number,
                               result=f(number),
                               elapsed_time=str(time.time() - tick))

    return {"work_id": work.id}
