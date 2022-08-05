# PC上のDockerでWebサーバを実行する

PC上のDockerでWebサーバを実行しましょう。
Dockerを使うことで、自分のPC以外でも実行するのが簡単になります。

## 1. Webサーバが依存しているライブラリを記述する

前準備として、Webサーバが依存しているライブラリを記述したファイルrequirements.txtを用意します。このファイルの役割は、ライブラリのバージョンを固定することです。バージョンを固定しないとWebサーバのビルド時に最新のライブラリが使われますが、それだとWebサーバが動作しなくなることがあります。

```
fastapi == 0.79.0
uvicorn[standard] == 0.17.6 
gunicorn == 20.1.0
```

```fastapi[all]```としないのは、これだと不要なライブラリまでインストールしてしまうからです。このファイルがある場所で、以下のコマンドを実行すると依存ライブラリをまとめてインストールできます。

```sh
pip install -r requirements.txt
```

## 2. Dockerfileを記述する

Docker Imageを作るためのコマンドを書いたファイル「Dockerfile」を追加します。内容は以下とします。

```docker
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
```


## 3. Docker Imageのビルド/コンテナの起動・停止を簡単に行えるようにする

docker-compose.ymlを以下の内容で作ってください。

```yaml
version: '3'

services:
  api:
    container_name: python-api-server
    build: .
    environment:
      PORT: 8000
    ports:
      - "8000:8000"
```

## 4. PC上のDockerでWebサーバを実行する

以下のコマンドを実行すると、Webサーバを起動できます。

```sh
docker compose up api
```

Webブラウザで"http://127.0.0.1:8000/?q=test"を開いてください。PC上で直接Webサーバを実行したときと同じ動作になれば正常です。

## 5. GitHubに変更を保存する

```sh
git add requirements.txt Dockerfile docker-compose.yml
git commit -m "tutorial 1-3"
git push
```
