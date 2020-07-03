import dj_database_url
import environ

from .base import *

# Herokuに設定した環境変数を読み込む
env = environ.Env()

#  SECRET_KEYはHerokuの環境設定から設定
SECRET_KEY = env('SECRET_KEY')

# 本番環境ではデバッグをFalseにする
DEBUG = False

# ALLOWED_HOSTSはHerokuの環境設定から設定
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# HerokuのPostgres_URLを設定
DATABASES = {
    'default': dj_database_url.config()
}
