# django-react-boilerplate



## Backend

### Info

- Python 3.8.10
- Django 3.2.5
- anaconda 4.9.2

### settings

- config/settings
  - base
  - dev
  - prod

### requirements

- requirements/common.txt
- requirements/dev.txt
- requirements/prod.txt

### env

- common/env.json
  - development
  - product

### env_format

```json
{
  "development": {
    "SECRET_KEY": "abcdefg",
    "DATABASES": {
      "default": {
       "ENGINE": "engine",
			 "NAME": "name",
			 "USER": "username",
       "PASSWORD": "password",
  		 "HOST": "",
  		 "PORT": ""
      }
    }
  }
}
```

### Package

**base**

- Django
- djangoframework
- djangorestframework-jwt
- django-cors-headers
- pillow
- psycopg2

**dev**

- django-debug-toolbar
- httpie



## Frontend

- TypeScript
- React



## Setting Guide

1. config/common/env.json 파일 이동
2. 아나콘다 가상환경 생성
   1. `$ conda create --name 프로젝트명 python=파이썬 버전` 
3. 가상환경 활성화
   1. `$ conda activate 프로젝트명`
   2. `$ conda deactivate 프로젝트명` 비활성
4. 패키지 파일 설치
   1. `$ pip install -r requirements.txt`
5. 환경변수 설정
   1. `DJANGO_SETTINGS_MODULE=config.settings.base;SERVER_ENV=Local;`
6. backend 서버
   1. `$ python manage.py runserver`
7. frontend 서버
   1. `$ yarn react-scripts start`
      1. 포트 설정시 react-scripts start 앞에 export PORT=포트번호

