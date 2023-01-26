# Beringlab 과제

## 요약
피보나치수열의 n번째 해당하는 값을 저장하는 api 가 있을 때, 비동기적으로 동작하도록 수정하라.

## 스택
`Django` `celery` `rabbitmq` `redis` `sqlite3`

- rabbitmq 로 task 관리하며 redis 로 결과를 받도록 구현.
- docker 를 이용하여 `rabbitmq` 와 `redis` 를 실행하도록 구현.

## 실행

### Broker & Backend
```bash
# rabbitmq docker 실행.
docker run -d -p --name rmq_server 5672:5672 -p 15672:15672 rabbitmq

# rabbitmq web 접근 허용
docker exec rmq_server rabbitmq-plugins enable rabbitmq_management

# redis docker 실행.
docker run -d -p --name redis_server 6379:6379 redis
```

### django
```bash
pip3 install -r requirements.txt
python3 manage.py runserver
# http://localhost:8000/works 에 접속하여 작업 요청
# http://localhost:8000/tasks/<task_id>/ 에 접속하여 작업 결과 확인
```