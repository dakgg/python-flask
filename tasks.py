from celery import Celery
import os

# 결과 저장 경로 만들기
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RESULT_BACKEND_PATH = f'file://{BASE_DIR}/celery_results'

celery_app = Celery(
    'tasks',
    broker='memory://', # 메모리 큐 (개발용)
    backend=RESULT_BACKEND_PATH # 파일 기반 결과 저장 (JSON)
)

@celery_app.task
def add(x, y):
    return {"sum": x + y}