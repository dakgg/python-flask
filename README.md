# python-flask

# How to Init
```shell
python3 -m venv venv # 가상환경 설치
source venv/bin/activate # 가상환경 시작
pip install -r requirements.txt # 패키지 설치
deactivate # 가상환경 종료
```
### 레디스
```shell
brew install redis
brew services start redis
```

## 앱 시작
```shell
python app.py
```
or
```shell
python3 app.py
```

## 셀러리 시작
```shell
source venv/bin/activate 
celery -A tasks.celery_app worker --loglevel=info
```

## Post 보내기
```shell
curl -X POST http://127.0.0.1:5000/add \
     -H "Content-Type: application/json" \
     -d '{"x": 2, "y": 3}'
```