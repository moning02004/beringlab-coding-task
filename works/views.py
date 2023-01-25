import random

from django.http import HttpResponse

from beringlab.celery import app


def process_work(request):
    n = random.randrange(35, 42)
    task_id = app.send_task("works.tasks.fibonacci", queue="fibonacci", kwargs={
        "number": n
    })
    message = f"요청을 수행하고 있습니다. task_id: {task_id}"
    return HttpResponse(message)
