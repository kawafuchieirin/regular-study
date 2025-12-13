# セッション２: Docker Hello World

このセッションでは、Dockerの公式hello-worldイメージをpullして実行します。

## 手順

### 1. hello-worldイメージをpullする

```bash
docker pull hello-world
```

### 2. hello-worldコンテナを実行する

```bash
docker run hello-world
```

## 説明

- `docker pull hello-world`: Docker Hubからhello-worldイメージをダウンロードします
- `docker run hello-world`: ダウンロードしたイメージからコンテナを起動して実行します

実行すると、Hello Worldのメッセージが表示されます。

## 補足

初めて実行する場合、`docker run hello-world`を実行すると、イメージが存在しない場合は自動的にpullされます。
そのため、`docker pull hello-world`のステップは省略可能です。

