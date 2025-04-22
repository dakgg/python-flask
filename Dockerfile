FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# flask
EXPOSE 7777
# debugpy
EXPOSE 3920 

# 기존 pip 설치 후에 추가
RUN pip install debugpy

CMD ["flask", "run"]