# pythonの最新版をベースに使用
FROM python:latest

# 作業ディレクトリ作成
WORKDIR /workdir

# パッケージ情報の更新とsudoのインストール
RUN apt-get update && apt-get install -y sudo

# pipをアップグレード
RUN pip install --upgrade pip

COPY requirements.txt /workdir
RUN pip install -r requirements.txt
