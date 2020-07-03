import dj_database_url
import environ

from .base import *

# .envからSECRET_KEYを読み込む
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

# 本番環境ではデバッグをFalseにする
DEBUG = False

# 本番環境ではドメインからのアクセスのみ許可
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# HerokuのPostgres_URLを読み込む
DATABASES = {
    'default': dj_database_url.config()
}
