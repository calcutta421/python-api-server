# PC上でWebサーバを実行する

Webサーバは、Web FrameworkのFast APIを使って作ります。
Webサーバを0から作るのは大変ですが、Web Frameworkを作ることで楽に実装することができます。

## 1. Fast APIをPCにインストールする

以下のコマンドを実行してFast APIをインストールしてください。

```sh
pip install "fastapi[all]"
```

## 2. Webサーバのコードを記述する

次に、トップディレクトリにmain.pyというファイルを作り、以下の記述をしてください。

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## 3. Webサーバを起動する

以下のコマンドでWebサーバを起動してください。

```sh
uvicorn main:app --reload
```

## 4. Webサーバにアクセスする

"http://127.0.0.1:8000/"をWebブラウザで開いてください。
以下のテキストが表示されたら成功です。

```
{"message": "Hello World"}
```

## 5. GitHubに変更を保存する

```sh
git add main.py
git commit -m "tutorial 1-1"
git push
```

## 備考

ここで返しているレスポンスの形式をJSON(JavaScript Object Notation)と呼びます。JSONはプログラムにとって使いやすい形式です。
人間が読むWebページを表示するのではなく、他のプログラムに機能を提供することが目的であれば、JSONは良い選択肢の1つです。

「他のプログラムに機能を提供する」仕組みをAPI(Application Programming Interface)と呼びます。Webを使うことを明示したいときは、Web APIと呼びます。