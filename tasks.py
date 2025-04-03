from celery import Celery

celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',   # 브로커 (작업 큐)
    backend='redis://localhost:6379/0'   # 결과 저장소
)

@celery_app.task
def add(x, y):
    return {"sum": x + y}