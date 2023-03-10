import random

from celery.result import AsyncResult
from django.http import HttpResponse

from works.models import Work
from works.tasks import fibonacci


def process_work(request):
    n = random.randrange(35, 42)
    task = fibonacci.apply_async(kwargs={"number": n}, queue="fibonacci")
    message = f"요청을 수행하고 있습니다. task_id: {task.id}"
    return HttpResponse(message + f"<br><br> - <a href=\"/tasks/{task.id}\">요청 결과 확인하기</a>")


def check_task(request, task_id):
    task = AsyncResult(task_id)
    if str(task.status).lower() == "success":
        try:
            work = Work.objects.get(pk=task.result["work_id"])
            message = f"요청이 완료되었습니다.<br><br>- 걸린 시간: {work.elapsed_time}<br>- {work.n} 번째 값: {work.result}"
        except Work.DoesNotExist:
            message = f"데이터가 존재하지 않습니다."
    else:
        message = "요청을 수행중입니다."
    return HttpResponse(message)
