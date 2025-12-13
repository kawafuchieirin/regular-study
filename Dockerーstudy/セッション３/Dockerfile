# ベースイメージの指定
# python:3.11-slim は軽量なPython実行環境を提供
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# ホストのファイルをコンテナにコピー
COPY hello.py .

# コンテナ起動時に実行するコマンド
CMD ["python", "hello.py"]

