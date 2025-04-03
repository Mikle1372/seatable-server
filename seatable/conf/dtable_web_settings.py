
IS_PRO_VERSION = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'mariadb',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'Rossia',
        'NAME': 'dtable_db',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379',
    }
}

SECRET_KEY = '04!^vmz2q#l#+vpi!yvy!66e7r$=n=v)#uiypw3q$uii4jkj8s'

# for dtable-server
DTABLE_PRIVATE_KEY = 'f0b#t7m&=br9#*@swz!wo4&9f)9vp@k*g09c!)1k#u&&a+#rx1'
DTABLE_SERVER_URL = 'https://unilight-seatable.ru/dtable-server/'
DTABLE_SOCKET_URL = 'https://unilight-seatable.ru/'

# for dtable-web
DTABLE_WEB_SERVICE_URL = 'https://unilight-seatable.ru/'

# for dtable-db
DTABLE_DB_URL = 'https://unilight-seatable.ru/dtable-db/'

# for dtable-storage-server
DTABLE_STORAGE_SERVER_URL = 'http://127.0.0.1:6666/'

NEW_DTABLE_IN_STORAGE_SERVER = True

# for seaf-server
FILE_SERVER_ROOT = 'https://unilight-seatable.ru/seafhttp/'

ENABLE_USER_TO_SET_NUMBER_SEPARATOR = True

TIME_ZONE = 'Europe/Moscow'

DISABLE_ADDRESSBOOK_V1 = True
ENABLE_ADDRESSBOOK_V2 = True


PLUGINS_REPO_ID='cd05de79-3f9b-48e4-9a6c-5e379feba3a6'
