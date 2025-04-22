# Python Flask + Docker Sample Project

## 📚 정의
Flask와 Docker를 활용한 기본 애플리케이션 프로젝트입니다.

- REST API 테스트
- Docker를 이용한 환경 구성


## 파일 구조
```
├── app.py               # Flask 메인 애플리케이션
├── tasks.py             # 백그라운드 작업 (비어있을 것임)
├── requirements.txt     # 필요 패키지 목록
├── Dockerfile           # Docker 이미지 빌드 설정
└── docker-compose.yml   # Docker Compose 환경 설정
```

# 어플리케이션 실행
``` bash
docker-compose up --build
```

# 테스트 방식
## POST /add
- http://127.0.0.1:7777/add
- 요청 형식
``` json
{
  "x": 2,
  "y": 3
}
```
- 응답 형식
``` json
{
  "result": 5
}
```

``` bash
curl -X POST http://127.0.0.1:7777/add -H "Content-Type: application/json" -d '{"x": 2, "y": 3}'
```
