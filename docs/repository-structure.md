# リポジトリ構成図

このリポジトリの主要なディレクトリとファイルの構成をまとめています。

## 全体構成

```text
regular-study/
├── .claude/
│   └── skills/
│       └── output/
│           └── SKILL.md
├── .github/
│   └── workflows/
│       └── pre-commit.yml
├── Study_Lesson/
│   └── Dockerーstudy/
├── output/
│   └── profile.md
├── CLAUDE.md
├── README.md
└── repository-structure.md
```

## ディレクトリごとの役割

| パス | 役割 |
| --- | --- |
| `.claude/` | Claude Code 用のローカル設定・スキル定義 |
| `.github/workflows/` | GitHub Actions のワークフロー定義 |
| `Study_Lesson/` | 過去勉強会資料のアーカイブ |
| `Study_Lesson/Dockerーstudy/` | Docker 学習用のセッション別資料 |
| `output/` | 学習アウトプットや生成結果の置き場 |
| `README.md` | 勉強会の概要、ルール、テーマ一覧 |
| `CLAUDE.md` | このリポジトリを扱う補助エージェント向けのメモ |

## Docker 学習資料の見方

`Study_Lesson/Dockerーstudy/` 配下は、セッションごとに段階的に学べるよう構成されています。

| パス | 内容 |
| --- | --- |
| `セッション２/` | セッション 2 の説明資料 |
| `セッション３/` | Dockerfile と簡単な Python 実行例 |
| `セッション４/` | セッション 4 の説明資料 |
| `セッション５/` | Python アプリを Docker 化するサンプル |
| `セッション6/` | `docker-compose.yml` を含む複数ファイル構成の例 |
| `アウトプット用/` | 受講者や作業用の成果物置き場 |

## 補足

- `.git/` や `.DS_Store` などの管理用ファイルは構成図から省略しています。
- この構成図は 2026-04-19 時点のワークツリーをもとに作成しています。
