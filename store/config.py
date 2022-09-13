import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일을 읽어서 환경변수에 넣어줌

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["STORE_DATABASE_NAME"],
        "USER": os.environ["STORE_DATABASE_USER"],
        "PASSWORD": os.environ["STORE_DATABASE_PASSWORD"],
        "HOST": os.environ["STORE_DATABASE_HOST"],
        "PORT": int(os.environ.get("STORE_DATABASE_PORT", "3306")),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

SECRET_KEY = os.environ["STORE_SECRET_KEY"]
