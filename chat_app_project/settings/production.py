import environ
from .development import *


env = environ.Env(DEBUG=(bool, False))

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

DATABASES = {"default": env.db("DATABASE_URL")}

ALLOWED_HOSTS = ['www.chat-djangoapp.herokuapp.com','chat-djangoapp.herokuapp.com']

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env("REDIS_URL")],
        },
    }
}
