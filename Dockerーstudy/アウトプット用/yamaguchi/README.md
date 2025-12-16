# Simple BMI API (Flask + Docker)

Docker を使って簡単に動かせる、シンプルな Flask API です。
`height` と `weight` をもとに BMI を計算します。

## Build

```bash
docker build -t simple-bmi-api .
```

## Run

```bash
docker run --rm -p 3000:3000 simple-bmi-api
```

## Try it

```bash
curl http://localhost:3000/healthz
curl "http://localhost:3000/bmi?height=170&weight=65"
```
