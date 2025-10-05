# Learning "Cracking the Coding Interview" with Codex & ChatGPT

## Overview
I am studying *Cracking the Coding Interview* using a combination of Codex (for code automation) and ChatGPT (for exploration and refinement). This workflow lets me focus on solving every exercise from scratch while still leveraging AI to design reliable tests and produce polished reference solutions.

## Environment Setup
- Manage dependencies with `uv` and the existing `pyproject.toml` file.
- Install any required packages via `uv pip install` or by syncing the project with `uv sync`.

## Study Workflow
1. Checkout the `problem_only` branch and create the target directory plus a `problem.py` that contains the copied problem statement in its docstring.
2. Still on `problem_only`, ask Codex to design the public function signatures and author the colocated `test_problem.py`; stage, commit, and push the scaffolding to `origin problem_only`, then switch back to `feature_full_workflow`.
3. On `feature_full_workflow`, implement the full solution in `problem.py`, then run `pytest test_problem.py` (or the appropriate path) to verify the implementation.
4. Once the tests pass, treat the solution as complete. Optionally share the finished `problem.py` with ChatGPT to obtain a more elegant or efficient take on the problem.
5. (Optional) Save that refined solution into `best_answer_by_LLM.py` for future reference and comparison; keep these enhancements on `feature_full_workflow`.

---

# CodexとChatGPTで「世界で戦うプログラミング力を鍛える本」を学ぶ

## 概要
Codex（コード自動化）とChatGPT（考察・洗練）を組み合わせて「世界で戦うプログラミング力を鍛える本」を学習しています。各問題について自力で実装しつつ、AIを活用してテスト設計と模範解答の収集を行います。

## 環境構築
- 依存関係は `uv` と既存の `pyproject.toml` で管理します。
- 必要なパッケージは `uv pip install` もしくは `uv sync` でインストールします。

## 学習の流れ
1. `problem_only` ブランチにチェックアウトし、対象ディレクトリと `problem.py` を用意して問題文をドキュメント文字列として貼り付けます。
2. 同じく `problem_only` 上で Codex に関数の入出力仕様と `test_problem.py` のテストケース作成を依頼し、ステージ → コミット → `git push origin problem_only` まで完了させたら `feature_full_workflow` に戻ります。
3. `feature_full_workflow` に切り替えて `problem.py` に自分の実装を書き、`pytest test_problem.py`（または該当パス）で検証します。
4. テストが通れば回答完了とし、さらに効率的・エレガントな解法を得たい場合は `problem.py` を ChatGPT に共有して提案を受けます。
5. （任意）得られた解法を `best_answer_by_LLM.py` に保存し、比較・振り返りに活用します。これらの拡張は `feature_full_workflow` で管理します。
