# AGENT Notes

## Branch Strategy
- Maintain two long-lived branches:
  - `problem_only`: contains problem statements and Codex-authored tests (Study Workflow steps 1 & 2). Keep this branch clean so that each exercise starts from scratch.
  - `feature_full_workflow`: includes everything on `problem_only` plus your personal implementations, ChatGPT refinements, and any auxiliary study files (e.g., `best_answer_by_LLM.py`).
- When beginning a new exercise, checkout `problem_only` (`git checkout problem_only`) and do all scaffolding work there. Once the docstring and tests are ready, **commit and push to the remote `problem_only` branch** (e.g., `git commit ...` followed by `git push origin problem_only`).
- After pushing the scaffolding, immediately switch back to `feature_full_workflow` (`git checkout feature_full_workflow`) before starting your solution work or additional experimentation.
- For hands-on practice, solutions, and experimentation, work on `feature_full_workflow` (either directly or via feature branches that merge into it). Push that branch when the enhanced workflow is ready to share.

## Study Workflow Recap
1. On `problem_only`, create/update the exercise directory and `problem.py` docstring.
2. Still on `problem_only`, ask Codex for function signatures and `test_problem.py`; stage, commit, and push these scaffolding changes to `origin problem_only`.
3. Switch to `feature_full_workflow`, implement the solution, and run `pytest practice/ChXX/<section>/test_problem.py` to verify.
4. Share the finished solution with ChatGPT for refinement; optionally store the improved version in `best_answer_by_LLM.py` on `feature_full_workflow`.

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
- 新しい設問に取り組むときは必ず `problem_only` にチェックアウトし、スキャフォールディング（問題文とテスト）を整備する。準備が整ったら **`problem_only` でコミットし、`git push origin problem_only` でリモートに反映** する。
- プッシュが終わったらすぐに `feature_full_workflow` に戻って (`git checkout feature_full_workflow`)、実装や追加検証を進める。
- 実際の実装・実験は `feature_full_workflow` 側（必要なら派生ブランチ）で行い、仕上がったらプッシュする。

## 学習フロー再確認
1. `problem_only` 上で `problem.py` に問題文を貼り、ディレクトリを整える。
2. 同じく `problem_only` 上で Codex に `test_problem.py` とインタフェース設計を依頼し、ステージ → コミット → `git push origin problem_only`。
3. `feature_full_workflow` に切り替えて実装 → `pytest practice/ChXX/<section>/test_problem.py` で検証。
4. 完成した実装を ChatGPT に渡して洗練案をもらい、必要なら `feature_full_workflow` 上で `best_answer_by_LLM.py` に保存。

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
