# AGENT Notes

## Branch Strategy
- Maintain two long-lived branches:
  - `problem_only`: contains problem statements and Codex-authored tests (Study Workflow steps 1 & 2). Keep this branch clean so that each exercise starts from scratch.
  - `feature_full_workflow`: includes everything on `problem_only` plus your personal implementations, ChatGPT refinements, and any auxiliary study files (e.g., `best_answer_by_LLM.py`).
- When beginning a new exercise, switch to `problem_only` (`git checkout problem_only`) and create a feature branch from there if needed. After adding/adjusting problem statements and tests, commit and push back to the remote `problem_only` branch.
- For hands-on practice, solutions, and experimentation, work on `feature_full_workflow` (either directly or via feature branches that merge into it). Push the polished study branch when ready.

## Study Workflow Recap
1. Create/update the exercise directory and `problem.py` docstring on `problem_only`.
2. Ask Codex for function signatures and `test_problem.py` in the same folder; commit/push to `problem_only` when the scaffolding is ready.
3. Switch to `feature_full_workflow`, implement the solution, and run `pytest practice/Ch[**]/<section>/test_problem.py` to verify.
4. Share the finished solution with ChatGPT for refinement; optionally store the improved version in `best_answer_by_LLM.py`.

## Environment
- Use `uv` with `pyproject.toml` / `uv.lock` to manage dependencies (`uv sync`, `uv pip install ...`).
- `pytest` is the primary test runner.

## File Layout Expectations
- Each problem directory (e.g., `practice/Ch01/1.1/`) contains: `problem.py`, `test_problem.py`, optional `best_answer_by_LLM.py`.
- Tests import solutions via dynamic loading; keep function names consistent with the docstring instructions.

## Operational Tips
- Avoid leaving compiled `__pycache__` directories in commits; clean them before staging.
- Keep README.md aligned with workflow changes.
- When introducing new exercises, replicate the existing pattern to keep both branches synchronized.

---

# エージェントメモ（日本語）

## ブランチ運用
- 長期運用するブランチは2本:
  - `problem_only`: 問題文とテストだけを含む（学習フローの Step1 & 2）。常にクリーンな状態を保つ。
  - `feature_full_workflow`: `problem_only` の内容に加え、実装コードや ChatGPT による改良案、`best_answer_by_LLM.py` など学習補助ファイルを配置。
- 新しい設問に取り組むときは `problem_only` にチェックアウトして作業し、準備が整ったらコミット＆プッシュ。
- 実際の実装や追加検証は `feature_full_workflow` 側で行い、適宜プッシュ。

## 学習フロー再確認
1. `problem.py` に問題文を貼り、`problem_only` 上でディレクトリを整える。
2. Codex に `test_problem.py` とインタフェース設計を依頼し、`problem_only` にコミット＆プッシュ。
3. `feature_full_workflow` に切り替えて実装 → `pytest practice/Ch01/<section>/test_problem.py` で検証。
4. 完成した実装を ChatGPT に渡して洗練案をもらい、必要なら `best_answer_by_LLM.py` に保存。

## 環境
- 依存関係は `uv` + `pyproject.toml` / `uv.lock` で管理（`uv sync`, `uv pip install ...`）。
- テストは `pytest` を使用。

## ファイル構成
- 各問題ディレクトリ: `problem.py`, `test_problem.py`, 任意で `best_answer_by_LLM.py`。
- テストは動的ロードなので、公開関数名はドキュメントと一致させる。

## 運用メモ
- コミット前に `__pycache__` を削除する。
- README.md をフローの更新と同期させる。
- 新問題を追加する際は既存の構造を再利用し、両ブランチを同期。
