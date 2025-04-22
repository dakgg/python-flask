# python-flask

# How to Init
```shell
docker-compose up --build
```

## Post 보내기
```shell
curl -X POST http://127.0.0.1:7777/add \
     -H "Content-Type: application/json" \
     -d '{"x": 2, "y": 3}'
```