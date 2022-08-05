# Overview

Webサーバを構築してみましょう。全体構成は以下とします。

<図>

Webサーバとは、「利用者側のコンピュータに対しネットワークを通じて情報や機能を提供するコンピュータおよびソフトウェア」のことです。
例は、Webブラウザ開いたページの中身を返すソフトウェアです。
Webサーバは、PythonとWeb FrameworkのFast APIで作ります。

GitHubは、ソースコードをホスティングするサービスです。ここにWebサーバのソースコードを置きます。
バージョン管理ツールGitに対応しており、ソースコードの変更履歴を見たり、過去のバージョンに戻したり、他人とソースコードを共有することができます。

サーバはGoogle Cloud Platform(GCP)で動かします。
GCPは様々なサービスの集合で、アカウント管理、Webサーバを実行するためのインフラなどを提供します。
なお、クラウドとは「ソフトウェア開発者がインフラを持たなくても、インターネットを通じて、サービスを必要な時に必要な分だけ利用する考え方」です。

Cloud Buildは、GCPのCI/CD(Continuous Integration/Continuous Deployment)サービスです。
複数人開発時にソースコードの統合を頻繁にしたり、変更をすぐにソフトウェアに適用することを支援してくれます。
GitHubなどでホスティングされているソースコードの変更を検知し、ソースコードからWebサーバのDocker ImageをビルドしてCloud Runにデプロイします。
Dockerについては、[Dockerの日本語ドキュメントの説明に譲ります。](https://docs.docker.jp/v1.11/engine/understanding-docker.html)

Container Registryは、GCPが提供するDocker Imageのホスティングサービスです。

Cloud Runは、GCPが提供するDocker Imageの実行環境です。
Docker ImageのホスティングサービスからDocker Imageを入手し、そこからContaierを作って実行します。
WebサーバへWebブラウザなどからアクセスできるようにもしてくれます。

## 環境構築

以下のツールをインストールしてください。

- Python3
- Visual Studio Code
- Git

その後、以下のユーザアカウントを作ってください。

- GitHub
- GCP

以下のコマンドを実行して、本リポジトリをclone&初期化してください。

```
git clone git@github.com:KamikazeZirou/python-api-server.git
cd python-api-server
git checkout 292d9b8ede951868c7806e6d3302ca5ed0d21e51
```

## 3. Webサーバを公開する

## 4. WebサーバのアクセスをBasic認証で制限する

## 5. Webサーバのアクセスをアカウントで制限する