import environ
from .development import *


env = environ.Env(DEBUG=(bool, False))

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

DATABASES = {"default": env.db("DATABASE_URL")}

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['chatapp.eniola.xyz'])
