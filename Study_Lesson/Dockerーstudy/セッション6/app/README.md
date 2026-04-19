コマンド

## 起動
```
docker-compose up --build
```

サンプルリクエスト
```
curl -X POST -G \
  --data-urlencode "text=最近買ってよかったものは？" \
  --data-urlencode "category=talk" \
  http://localhost:8000/topics

```

```
curl -X POST -G \
  --data-urlencode "text=今までで一番ハマったゲームは？" \
  --data-urlencode "category=game" \
  http://localhost:8000/topics

```

```
curl -X POST -G \
  --data-urlencode "text=無人島 に1つ持っていくなら？" \
  --data-urlencode "category=talk" \
  http://localhost:8000/topics

```

お題を取得
```
curl "http://localhost:8000/topics/random"
```
