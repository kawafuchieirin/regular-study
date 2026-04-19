# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

## リポジトリ概要

かわふちの定期勉強会用リポジトリです。GitHubの使い方や開発環境についての学習を目的としています。

## リポジトリ構成

- `README.md` - 勉強会のルールとテーマ一覧
- `.pre-commit-config.yaml` - pre-commit設定
- `.github/workflows/pre-commit.yml` - CI設定

## 開発コマンド

```bash
# pre-commitのインストール
pip install pre-commit

# pre-commitフックのセットアップ
pre-commit install

# 全ファイルに対してpre-commitを手動実行
pre-commit run --all-files
```

## CI/CD

PRとmainブランチへのpushで自動的にpre-commitチェックが実行されます。

チェック内容：

- 汎用: trailing whitespace, ファイル末尾改行, YAML/JSON構文
- Python: black, isort, flake8
- Markdown: markdownlint

### Release Drafter

- `.github/workflows/release-drafter.yml` が main への push 時に release-drafter を実行し、ドラフト Release を自動更新
- PR タイトルを Conventional Commits（`feat:` / `fix:` / `docs:` / `chore:` など）で書くと autolabeler が自動でラベル付与
- 設定は `.github/release-drafter.yml`。ドラフトは GitHub UI から手動で Publish してタグ発行

## 勉強会テーマの追跡

各回の勉強会内容はGitHub Issuesで管理されています。新しい勉強会を追加する場合は、README.mdのテーブルにリンクを追加してください。
