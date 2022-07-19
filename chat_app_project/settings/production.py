import environ
from .development import *


env = environ.Env(DEBUG=(bool, False))

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddfj19h06063va', 
        'USER': 'lgntkaraxrrtti', 
        'PASSWORD': '8fb5d9a60d59573d40d109ec6a5af9bbb99f3ded8eacf9b689f0222dc900b05f',
        'HOST': 'ec2-3-223-169-166.compute-1.amazonaws.com', 
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['www.chat-djangoapp.herokuapp.com','chat-djangoapp.herokuapp.com']

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("REDIS_URL")],
        },
    }
}
