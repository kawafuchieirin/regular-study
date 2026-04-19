#!/usr/bin/env bash
set -euo pipefail

# regular-study 初期設定スクリプト
# - mise で Python と pre-commit をインストール
# - .mise.toml の postinstall フックで pre-commit の git hook も自動登録される

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

info()  { printf '\033[1;34m[INFO]\033[0m %s\n' "$*"; }
ok()    { printf '\033[1;32m[ OK ]\033[0m %s\n' "$*"; }
err()   { printf '\033[1;31m[FAIL]\033[0m %s\n' "$*" >&2; }

# 1. mise の存在確認
if ! command -v mise >/dev/null 2>&1; then
  err "mise が見つかりません。先にインストールしてください: https://mise.jdx.dev/installing-mise.html"
  err "  例: brew install mise"
  exit 1
fi
ok "mise: $(mise --version)"

# 2. .mise.toml を trust（初回のみ対話的に必要なため明示的に実行）
info ".mise.toml を trust します"
mise trust "$SCRIPT_DIR/.mise.toml"

# 3. ツールのインストール（python / pre-commit）
#    postinstall フックで 'pre-commit install' が自動実行される
info "mise install を実行します（Python / pre-commit）"
mise install

# 4. 検証
info "インストール結果を検証します"
mise exec -- python --version
mise exec -- pre-commit --version

if [ -x "$SCRIPT_DIR/.git/hooks/pre-commit" ]; then
  ok "git の pre-commit フックが有効化されています"
else
  err "git の pre-commit フックが未登録です。'mise install' を再実行してください"
  exit 1
fi

ok "初期設定が完了しました"
