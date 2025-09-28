# Learning "Cracking the Coding Interview" with Codex & ChatGPT

## Overview
I am studying *Cracking the Coding Interview* using a combination of Codex (for code automation) and ChatGPT (for exploration and refinement). This workflow lets me focus on solving every exercise from scratch while still leveraging AI to design reliable tests and produce polished reference solutions.

## Environment Setup
- Manage dependencies with `uv` and the existing `pyproject.toml` file.
- Install any required packages via `uv pip install` or by syncing the project with `uv sync`.

## Study Workflow
1. Create the target directory and a `problem.py` file for the current exercise, copying the problem statement into the docstring.
2. Ask Codex to design the public function signatures and author the associated `test_problem.py`, keeping the tests alongside the problem file.
3. Implement the full solution in `problem.py`, then run `pytest test_problem.py` (or the appropriate path) to verify the implementation.
4. Once the tests pass, treat the solution as complete. Optionally share the finished `problem.py` with ChatGPT to obtain a more elegant or efficient take on the problem.
5. (Optional) Save that refined solution into `best_answer_by_LLM.py` for future reference and comparison.

---

# CodexとChatGPTで「世界で戦うプログラミング力を鍛える本」を学ぶ

## 概要
Codex（コード自動化）とChatGPT（考察・洗練）を組み合わせて「世界で戦うプログラミング力を鍛える本」を学習しています。各問題について自力で実装しつつ、AIを活用してテスト設計と模範解答の収集を行います。

## 環境構築
- 依存関係は `uv` と既存の `pyproject.toml` で管理します。
- 必要なパッケージは `uv pip install` もしくは `uv sync` でインストールします。

## 学習の流れ
1. 対象ディレクトリと `problem.py` を用意し、問題文をドキュメント文字列として貼り付けます。
2. Codex に関数の入出力仕様と `test_problem.py` のテストケース作成を依頼します。テストは `problem.py` と同じ階層に置きます。
3. `problem.py` に自分の実装を書き、`pytest test_problem.py`（または該当パス）で検証します。
4. テストが通れば回答完了とし、さらに効率的・エレガントな解法を得たい場合は `problem.py` を ChatGPT に共有して提案を受けます。
5. （任意）得られた解法を `best_answer_by_LLM.py` に保存し、比較・振り返りに活用します。
