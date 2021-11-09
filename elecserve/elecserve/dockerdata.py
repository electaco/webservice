import os

class Database:
    ENGINE = os.getenv('DB_ENGINE') or 'django.db.backends.sqlite3'
    NAME = os.getenv('DB_NAME') or 'db.sqlite3'
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')

class Extra:
    SECRET_KEY = os.getenv('SECRET') or 'django-insecure-bfy-!0j095q-&l=(%jav4kbqgn2)=jl!k&zi5@aphjtq33yh8s'
    DEBUG = os.getenv('DEBUG', "True") == 'True'
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', "*").split(',')
    STATIC_ROOT = os.getenv('STATIC_ROOT', "static")