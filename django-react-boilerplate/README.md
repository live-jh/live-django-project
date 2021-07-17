# django-react-boilerplate



## Project Structure ver 0.0.1

```
├── backend														// django backend (하위 모델 추가)
│   └── account 											// [APP] 유저 앱 
├── config														// 설정
│   ├── common												// env file, 공통
│   └── settings											// base, dev, prod 서버 세팅
├── frontend
│   ├── public
│   └── src
│				├── api												// 프론트 api axios 모음
│				├── assets										// 프론트 에셋(font, css등)
│				├── redux											// 프론트 redux 설정
│				├── routes										// 프론트 router 설정
│				├── utils											// 프론트 공통 모듈 (날짜, 단위, 문자열, getLocalStorage등)
│				└── components								// 프론트 컴포넌트 (하위 페이지별 구분)
│		    		├── account								// 프론트 앱(페이지)
│				    │		├── presentationals		// 프론트 프레젠테이션 컴포넌트 (functinal component, 데이터 변경 작업 x)
│		        │		└── containers				// 프론트 컨테이너 컴포넌트 (class component, 데이터 변경, 추가)
│    				├── common								// 프론트 공통 컴포넌트 모음 (Modal, Alert, Noti)
│    				└── layouts								// 프론트 레이아웃 설정
├── manage.py								
├── requirements
│   ├── common.txt										// 공통 패키지 
│   ├── dev.txt												// 개발 패키지 
│   └── prod.txt											// 배포 패키지 설정
└── requirements.txt									// focus requriements/prod 
```



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

