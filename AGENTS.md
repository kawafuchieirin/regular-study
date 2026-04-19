# AGENTS.md

このファイルは Codex CLI 等の AI エージェントが本リポジトリで作業する際の指針です。
Claude Code 向けの詳細は `CLAUDE.md` を参照してください（本ファイルと内容は重複しません）。

## リポジトリ概要

定期勉強会用リポジトリ。GitHub の使い方や開発環境についての学習が目的。

## スキル一覧

このリポジトリには以下のスキルが定義されています。実体は `.claude/skills/<name>/SKILL.md`、`.codex/skills/<name>/SKILL.md` から相対 symlink で参照されており、Claude Code と Codex CLI で同一の手順書を共有します。

| スキル | 概要 |
|---|---|
| `output` | `output/` 配下の Markdown を元にスクール成果フォーマット5項目の文章を生成し Slack 投稿 |
| `create-issue` | `kawafuchieirin/regular-study` に GitHub Issue を作成。勉強会テーマは README.md の表にも追記 |

呼び出されたら、必ず該当する `.codex/skills/<name>/SKILL.md`（symlink 先 `.claude/skills/<name>/SKILL.md`）を Read で読み込み、記載されたすべてのステップを **順番通り** に実行してください。

### `output` スキル

ユーザーからの依頼例:
- 「output スキルを実行して」「output スキルを `<ファイル名>` で実行して」
- 「`output/<ファイル名>` をスクール成果フォーマットで Slack 投稿して」

ファイル名（例: `test.md`）が指定された場合、SKILL.md 内の `$ARGUMENTS` をそのファイル名として扱ってください。

必須環境変数（未設定時はエラーを表示し設定方法を案内）:
- `SLACK_USER_TOKEN`
- `SLACK_CHANNEL_ID`

確認の必須化:
- 生成した文章はユーザーから OK が出るまで Slack に投稿しないこと
- 投稿前に「Slack に投稿してよいですか？」と必ず確認すること

### `create-issue` スキル

ユーザーからの依頼例:
- 「イシューを作成して」「create-issue スキルを実行して」
- 「`<タイトル>` でイシュー立てて」

`$ARGUMENTS` はイシュータイトル候補として扱ってください。リポジトリは常に `kawafuchieirin/regular-study` 固定。

確認の必須化:
- ユーザー確認なしに `gh issue create` を実行しないこと
- 勉強会テーマの場合は README.md 更新後、コミット・プッシュもユーザー確認後のみ

### 新しいスキルを追加する場合

手順は `.codex/README.md` を参照してください。

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
