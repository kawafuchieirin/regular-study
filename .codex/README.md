# .codex/

OpenAI Codex CLI からこのリポジトリのスキルを利用するためのディレクトリです。

## 構成

```
.codex/
└── skills/
    └── output/
        └── SKILL.md → ../../../.claude/skills/output/SKILL.md  (symlink)
```

`SKILL.md` は `.claude/skills/output/SKILL.md` への **相対 symlink** です。
Claude Code と Codex CLI で同一のスキル定義を共有するため、ソース・オブ・トゥルースは `.claude/` 側の1ファイルに集約しています。

## 各ツールからの呼び出し方

| ツール | 呼び出し方 |
|---|---|
| Claude Code | `/output <ファイル名>` （`.claude/skills/output/SKILL.md` を自動検出） |
| Codex CLI | 「output スキルを `<ファイル名>` で実行して」と自然言語で依頼。Codex はリポジトリルートの `AGENTS.md` を自動読み込みし、その指示に従って `.codex/skills/output/SKILL.md` を Read して Step 1〜6 を実行します |

Codex CLI はプロジェクト配下のスラッシュコマンドをサポートしないため、`/output` 形式の呼び出しは Claude Code 限定です。

## スキルを編集する場合

`.claude/skills/output/SKILL.md` を直接編集してください。symlink 経由で Codex 側にも即座に反映されます。

## 新しいスキルを追加する場合

1. `.claude/skills/<name>/SKILL.md` を作成
2. `.codex/skills/<name>/` ディレクトリを作成し、相対 symlink を張る:

   ```bash
   mkdir -p .codex/skills/<name>
   ln -s ../../../.claude/skills/<name>/SKILL.md .codex/skills/<name>/SKILL.md
   ```

3. `AGENTS.md` に新スキルの呼び出し契約を追記

## Windows で clone する場合

git の symlink サポートを有効化してください:

```bash
git config --global core.symlinks true
```

macOS/Linux はデフォルトで有効です。
