# 개요
* 개발, 운영 설정을 .env파일로 분리

# 실행방법
* 개발
```shell
# 윈도우
set MODE=dev
uvicorn main:app

# 리눅스
export MODE=dev
uvicorn main:app
```

* 운영
```shell
# 윈도우
set MODE=prd
uvicorn main:app

# 리눅스
export MODE=prd
uvicorn main:app
```