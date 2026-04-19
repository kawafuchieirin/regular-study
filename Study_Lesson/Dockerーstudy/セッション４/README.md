# Docker基本コマンド体験ワーク

このREADMEは、**Docker未経験〜初学者**が
以下の基本コマンドを**実際に動かしながら理解する**ための体験ワークです。

* `docker run`
* `docker ps`
* `docker images`
* `docker stop`
* `docker rm`
* 基本的なオプション

公式Dockerイメージのみを使用し、確実に再現できる内容のみを記載しています。

---

## 事前条件

* Docker Desktop または Docker Engine が起動していること
* ターミナルを使用できること

  * macOS / Linux: Terminal
  * Windows: PowerShell または WSL

---

## ワーク全体の流れ

1. `docker run` でコンテナを起動する
2. `docker ps` でコンテナの状態を確認する
3. `docker images` でイメージを確認する
4. `docker stop` / `docker rm` で後片付けをする
5. 基本オプションを体験する

---

## 1. docker run を体験する

### 実行コマンド

```bash
docker run hello-world
```

### 確認内容

* `hello-world` イメージが自動的に取得される
* コンテナが1回実行されて終了する
* Dockerが正常に動作していることを確認できる

※ このコンテナは実行後すぐに停止します

---

## 2. docker ps を体験する

### 実行中のコンテナを確認

```bash
docker ps
```

* 何も表示されなければ正常です

### 停止中も含めて確認

```bash
docker ps -a
```

* `hello-world` の停止済みコンテナが表示されます

---

## 3. docker images を体験する

### 実行コマンド

```bash
docker images
```

### 確認内容

* `hello-world` イメージが一覧に表示される
* イメージはコンテナの元になるものです

---

## 4. 動き続けるコンテナを起動する

### nginx コンテナを起動

```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

### オプションの意味

| オプション             | 内容                 |
| ----------------- | ------------------ |
| `-d`              | バックグラウンドで実行        |
| `-p 8080:80`      | ホスト8080番 → コンテナ80番 |
| `--name my-nginx` | コンテナ名を指定           |

### 状態確認

```bash
docker ps
```

* `my-nginx` が実行中であることを確認

---

## 5. ブラウザで動作確認

ブラウザで以下にアクセスします。

```
http://localhost:8080
```

* **Welcome to nginx!** が表示されれば成功です

---

## 6. docker stop を体験する

### コンテナ停止

```bash
docker stop my-nginx
```

### 確認

```bash
docker ps
```

* 実行中コンテナ一覧から消えます

```bash
docker ps -a
```

* 停止状態で残っていることを確認

---

## 7. docker rm を体験する

### コンテナ削除

```bash
docker rm my-nginx
```

### 確認

```bash
docker ps -a
```

* `my-nginx` が一覧から消えます

---

## 8. よく使う基本オプション

| オプション    | 用途         |
| -------- | ---------- |
| `-d`     | バックグラウンド実行 |
| `-p`     | ポートフォワード   |
| `--name` | コンテナ名指定    |
| `-it`    | 対話操作       |

### 対話操作の例

```bash
docker run -it ubuntu bash
```

* Ubuntuコンテナ内のbashに入ります
* 終了は `exit`

---

## このワークで学べること

* Dockerコンテナの基本的なライフサイクル
* イメージとコンテナの違い
* 実務で頻出する基本コマンドとオプション

---

## 後片付け（任意）

不要になったイメージを削除する場合

```bash
docker rmi hello-world nginx ubuntu
```

※ 他で使用していない場合のみ実行してください
