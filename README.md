# Beringlab 과제

## 요약
피보나치 수열의 n번째 해당하는 값을 저장하는 api 가 있을 때, 비동기적으로 동작하도록 수정하라.

## 스택
`Django` `celery` `rabbitmq` `redis` `postgresql`

## 실행 전 준비
`rabbitmq` 와 `redis` 서버는 `beringlab/celery_settings.py` 에 정의하여 settings 에서 import 하였습니다.

`beringlab/celery_settings.py`는 `beringlab/celery_settings.py.example`을 참고하여 생성합니다.

## 실행
```bash
# docker 로 실행
docker-compose up --build -d

# http://localhost:8000 접속
```

```bash
# docker 로 실행하지 않을 시, rabbitmq, redis 를 따로 설치해주어야 합니다.

# docker 를 이용한 rabbitmq 실행 및 web ui 접근 허용
docker run -d --name rmq_server -p 5672:5672 -p 15672:15672 rabbitmq
docker exec rmq_server rabbitmq-plugins enable rabbitmq_management

# docker 를 이용한 redis 실행
docker run -d --name redis_server -p 6379:6379 redis

# 가상환경 생성 (생략 가능)
python3 -m venv venv 
source venv/bin/activate

# 패키지 설치
pip3 install -r requirements.txt

# celery worker 백그라운드로 실행
mkdir celery_files
celery multi start fibo_worker -A beringlab -l info -Q fibonacci -f ./celery_files/fibonacci.log --pidfile=./celery_files/fibonacci.pid

# 웹 실행
python3 manage.py runserver


```

## 구현

`/works` 에 접속하면 rabbitmq 에 작업을 넘겨 비동기적으로 동작하도록 구현했습니다.

또한, 결과를 받아볼 수 있도록 `/tasks/<task_id>` 를 추가하였습니다.

`web` container 와 `celery` container 가 같은 데이터베이스를 사용해야 하기에 `db` container 를 만들어 `postgresql` 를 사용했습니다.
