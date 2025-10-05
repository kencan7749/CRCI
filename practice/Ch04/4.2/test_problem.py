from __future__ import annotations

import importlib.util
import math
from pathlib import Path
from typing import Iterable, List, Optional

import pytest


MODULE_NAME = "ch04_4_2_problem"
NODE_CLASS_NAME = "Node"
FUNCTION_NAME = "minimal_bst"


def _load_problem_module():
    module_path = Path(__file__).with_name("problem.py")
    spec = importlib.util.spec_from_file_location(MODULE_NAME, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def problem_module():
    return _load_problem_module()


@pytest.fixture(scope="module")
def node_cls(problem_module):
    assert hasattr(problem_module, NODE_CLASS_NAME), "Define a Node class in problem.py"
    return getattr(problem_module, NODE_CLASS_NAME)


@pytest.fixture(scope="module")
def minimal_bst(problem_module):
    assert hasattr(problem_module, FUNCTION_NAME), "Define minimal_bst in problem.py"
    return getattr(problem_module, FUNCTION_NAME)


def inorder_values(root) -> List:
    if root is None:
        return []
    return inorder_values(root.left) + [root.value] + inorder_values(root.right)


def tree_height(root) -> int:
    if root is None:
        return -1  # height of empty tree in edges
    return 1 + max(tree_height(root.left), tree_height(root.right))


def assert_balanced(root):
    if root is None:
        return True
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    assert abs(left_height - right_height) <= 1
    assert_balanced(root.left)
    assert_balanced(root.right)


@pytest.mark.parametrize("values", [[], tuple(), ()])
def test_empty_iterable_returns_none(minimal_bst, values):
    assert minimal_bst(values) is None


def test_single_value(minimal_bst):
    root = minimal_bst([42])
    assert root is not None
    assert root.value == 42
    assert root.left is None and root.right is None


def test_inorder_matches_input(minimal_bst):
    values = list(range(1, 8))
    root = minimal_bst(values)
    assert inorder_values(root) == values
    # with odd length the root should be the middle element
    assert root.value == values[len(values) // 2]
    assert_balanced(root)


def test_even_length_allows_either_middle(minimal_bst):
    values = [1, 2, 3, 4, 5, 6]
    root = minimal_bst(values)
    assert inorder_values(root) == values
    assert root.value in {3, 4}
    assert_balanced(root)
    height = tree_height(root)
    max_allowed = math.ceil(math.log2(len(values) + 1))
    assert height <= max_allowed


def test_handles_duplicates(minimal_bst):
    values = [1, 1, 2, 3]
    root = minimal_bst(values)
    assert inorder_values(root) == values
    assert_balanced(root)
