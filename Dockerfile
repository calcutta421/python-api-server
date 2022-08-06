# Docker Imageのベース
FROM python:3.10-slim

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app

# ワーキングディレクトリの指定
WORKDIR $APP_HOME

# ソースコードをDocker Imageに組み込む
COPY main.py ./
COPY requirements.txt ./

# 依存ライブラリのインストール
RUN pip install --no-cache-dir -r requirements.txt

# Dockerコンテナの実行時のデフォルトコマンド
# Webサーバを起動するコマンド
CMD exec gunicorn -k uvicorn.workers.UvicornWorker --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
