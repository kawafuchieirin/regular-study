# Release Drafter ワークフロー仕様

PR をマージするたびに GitHub Release のドラフトを自動更新する仕組みの仕様書。

## 構成ファイル

| ファイル | 役割 |
|---|---|
| `.github/workflows/release-drafter.yml` | ワークフロー本体（トリガー・ジョブ定義） |
| `.github/release-drafter.yml` | release-drafter の動作設定（カテゴリ・ラベル・テンプレート） |

## トリガー

```yaml
on:
  pull_request:
    types: [opened, reopened, synchronize, closed]
```

`pull_request` イベントの 4 種すべてを受け、ジョブ側の `if:` 条件で役割を振り分ける。

| イベント | 実行されるジョブ |
|---|---|
| `opened` / `reopened` / `synchronize` | `autolabel` |
| `closed` かつ `merged == true` | `update_release_draft` |
| `closed` かつ `merged == false`（クローズのみ） | どちらも実行されない |

## ジョブ 1: `autolabel`

PR タイトルを見てラベルを自動付与する。

| 項目 | 値 |
|---|---|
| 実行条件 | `github.event.action != 'closed'` |
| Action | `release-drafter/release-drafter/autolabeler@v7` |
| 権限 | `contents: read` / `pull-requests: write` |

ラベル付与ルール（`.github/release-drafter.yml` の `autolabeler`）:

| PR タイトルのプレフィックス | 付与されるラベル |
|---|---|
| `feat:` / `feat(scope):` | `type: feature` |
| `fix:` / `fix(scope):` | `type: bug` |
| `docs:` / `docs(scope):` | `type: docs` |
| `chore:` / `refactor:` / `style:` / `test:` / `ci:` / `build:` | `type: maintenance` |
| 該当なし | ラベル無し（後述「その他変更」扱い） |

## ジョブ 2: `update_release_draft`

マージ済みの PR を集計して Release ドラフトを生成・更新する。

| 項目 | 値 |
|---|---|
| 実行条件 | `github.event.action == 'closed' && github.event.pull_request.merged == true` |
| Action | `release-drafter/release-drafter@v7` |
| 権限 | `contents: write` / `pull-requests: read` |
| `commitish` | `refs/heads/main` を明示 |

### 動作フロー

1. 既存の「最新ドラフト Release」を検索。無ければ新規作成
2. 前回 Publish 済み Release 以降のマージ済み PR を GitHub API から取得
3. 各 PR のラベルを `categories` 定義に従ってグルーピング
4. `version-resolver` でバージョンを決定
5. `template` に従って本文を組み立て、ドラフトを上書き更新

### カテゴリ分類

| ラベル | セクションタイトル |
|---|---|
| `type: feature` | 🚀 Features |
| `type: bug` | 🐛 Bug Fixes |
| `type: docs` | 📚 Documentation |
| `type: maintenance` / `type: dependencies` | 🧰 Maintenance |
| なし | 変更内容（未分類） |

### バージョン解決ルール

起点は前回 Publish 済み Release のタグ。初回は `v0.1.0` から開始。

| ラベルの存在 | bump レベル | 例（元が v0.1.0） |
|---|---|---|
| `type: breaking` | major | `v1.0.0` |
| `type: feature` | minor | `v0.2.0` |
| `type: bug` / `type: maintenance` / `type: docs` / `type: dependencies` | patch | `v0.1.1` |
| それ以外（ラベル無しのみ） | patch（default） | `v0.1.1` |

複数ラベルが混在する場合は **最も高位**（major > minor > patch）が採用される。

### 出力テンプレート

```
## 変更内容

- <PRタイトル> (#<番号>) @<author>
...

## 🚀 Features

- <PRタイトル> (#<番号>) @<author>

## 🐛 Bug Fixes

...

**Full Changelog**: <前回タグとの比較URL>
```

## Publish フロー

1. PR マージ → ドラフト Release が自動更新
2. 何度マージしても同じドラフトに蓄積される
3. リリースしたいタイミングで GitHub UI の **Releases → Edit → Publish release**
4. Publish 時に `tag_name` が Git タグとして自動発行
5. 次回以降の PR マージは新しいドラフト（次バージョン）として生成される

### CLI で Publish する場合

```bash
gh release edit <tag> --draft=false --latest
```

## 権限とトークン

- 使用トークン: `secrets.GITHUB_TOKEN`（Actions が自動発行、追加設定不要）
- PAT (Personal Access Token) や Secrets 登録は不要

## 運用ルール

### PR タイトル命名規則

Conventional Commits 形式で書くと自動ラベルが付く:

```
<type>(<scope>): <概要>
```

type の例: `feat` / `fix` / `docs` / `chore` / `refactor` / `test` / `ci` / `build`

### 手動ラベル調整

autolabeler のマッチを外したい場合や、ラベルを上書きしたい場合は PR 画面で手動でラベルを付け外し可能。次のワークフロー発火（synchronize 等）でも autolabeler は既存ラベルを上書きしない（追加のみ）。

### 過去 PR の遡及ラベル付け

v0.1.0 より前にマージ済みの PR にはラベルが付いていないため「変更内容」セクションに未分類で表示される。整理したい場合は GitHub UI で手動ラベル付け → `gh workflow run release-drafter.yml` で再実行。

## トラブルシューティング

| 症状 | 原因 | 対処 |
|---|---|---|
| `target_commitish invalid` エラー | PR イベントで本体 Action が走っている | autolabeler サブアクションに分離（本ワークフローは対応済み） |
| マージ直後のPRがドラフトから漏れる | GitHub の PR 索引化より早くワークフローが走る race condition | `pull_request: closed` トリガーに変更（本ワークフローは対応済み） |
| ラベルが付かない | PR タイトルが Conventional Commits 形式でない | タイトル修正 → `synchronize` イベントで再発火、または手動ラベル |
| ドラフトが2つできる | 前回 Publish 漏れ、または draft 手動削除で整合性崩れ | 古いドラフトを削除してから `gh workflow run` で再実行 |

## 参考

- [release-drafter/release-drafter](https://github.com/release-drafter/release-drafter)
- [Conventional Commits](https://www.conventionalcommits.org/ja/)
