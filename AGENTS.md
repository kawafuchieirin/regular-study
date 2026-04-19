# AGENTS.md

このファイルは Codex CLI 等の AI エージェントが本リポジトリで作業する際の指針です。
Claude Code 向けの詳細は `CLAUDE.md` を参照してください（本ファイルと内容は重複しません）。

## リポジトリ概要

定期勉強会用リポジトリ。GitHub の使い方や開発環境についての学習が目的。

## スキル: `output`

このリポジトリには「output」スキルが定義されています。
実体は `.claude/skills/output/SKILL.md`、`.codex/skills/output/SKILL.md` から相対 symlink で参照されており、Claude Code と Codex CLI で同一の手順書を共有します。

### 呼び出し契約

ユーザーから以下のような依頼を受けたら、必ず `.codex/skills/output/SKILL.md`（symlink 先 `.claude/skills/output/SKILL.md`）を Read で読み込み、記載された Step 1〜6 を **順番通り** に実行してください。

- 「output スキルを実行して」「output スキルを `<ファイル名>` で実行して」
- 「`output/<ファイル名>` をスクール成果フォーマットで Slack 投稿して」
- 同等の自然言語依頼

ファイル名（例: `test.md`）が指定された場合、SKILL.md 内の `$ARGUMENTS` をそのファイル名として扱ってください。

### 必須環境変数

Step 6 の Slack 投稿で以下を使用します。未設定時はエラーを表示し設定方法を案内すること。

- `SLACK_USER_TOKEN`
- `SLACK_CHANNEL_ID`

### ユーザー確認の必須化

- 生成した文章はユーザーから OK が出るまで Slack に投稿しないこと
- 投稿前に「Slack に投稿してよいですか？」と必ず確認すること

## 開発コマンド

```bash
# pre-commit セットアップ
pip install pre-commit
pre-commit install

# 全ファイルチェック
pre-commit run --all-files
```

## CI/CD

PR と main への push で pre-commit が自動実行されます（trailing whitespace、YAML/JSON 構文、black/isort/flake8、markdownlint 等）。
