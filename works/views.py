import random

from django.http import HttpResponse

from works.tasks import fibonacci


def process_work(request):
    n = random.randrange(35, 42)
    task = fibonacci.apply_async(kwargs={"number": n}, queue="fibonacci")
    message = f"요청을 수행하고 있습니다. task_id: {task.id}"
    return HttpResponse(message)
