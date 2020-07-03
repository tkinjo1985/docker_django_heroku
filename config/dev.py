import environ

from .base import *

# 環境変数ファイル.envを読み込み
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# .envから読み込み
SECRET_KEY = env('SECRET_KEY')

# 開発環境のためデバッグをTrueにする
DEBUG = True

# 全てのホストからのアクセスを許可
ALLOWED_HOSTS = ['*']

# .envから読み込み
DATABASES = {
    'default': env.db()
}
