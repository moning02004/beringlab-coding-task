# Beringlab 과제

## 요약
피보나치수열의 n번째 해당하는 값을 저장하는 api 가 있을 때, 비동기적으로 동작하도록 수정하라.

## 스택
`Django` `celery` `rabbitmq` `redis` `postgresql`

## 실행
`rabbitmq` 와 `redis` 서버는 `beringlab/celery_settings.py` 에 정의하여 settings 에서 import 하도록 구현했습니다.

`beringlab/celery_settings.py`는 `beringlab/celery_settings.py.example`을 참고하여 생성합니다.

```bash
# docker container 실행
docker-compose up -d
```

## 구현

`/works` 에 접속하면 rabbitmq 에 작업을 넘겨 비동기적으로 동작하도록 구현했습니다.

결과를 받아볼 수 있도록 `/tasks/<task_id>` 를 추가하였습니다.

`web` container 와 `celery` container 가 같은 데이터베이스를 사용해야 하기에 `postgresql` 를 사용했습니다.
