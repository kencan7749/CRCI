from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Iterable, List, Optional

import pytest


MODULE_NAME = "ch02_2_2_problem"
FUNCTION_NAME = "kth_to_last"
NODE_CLASS_NAME = "Node"


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


def build_linked_list(values: Iterable, node_cls):
    head = None
    prev = None
    for value in values:
        node = node_cls(value)
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head


def list_from_node(node) -> List:
    output: List = []
    current = node
    while current is not None:
        output.append(current.value)
        current = current.next
    return output


def call_kth(problem_module, node_cls, values: Iterable, k: int):
    func = getattr(problem_module, FUNCTION_NAME)
    head = build_linked_list(values, node_cls)
    return func(head, k)


def test_function_exists(problem_module):
    assert hasattr(problem_module, FUNCTION_NAME)


@pytest.mark.parametrize("values, k, expected", [
    ([1, 2, 3, 4, 5], 1, 5),
    ([1, 2, 3, 4, 5], 2, 4),
    ([1, 2, 3, 4, 5], 5, 1),
    (["a", "b", "c"], 2, "b"),
])
def test_returns_correct_value(problem_module, node_cls, values, k, expected):
    node = call_kth(problem_module, node_cls, values, k)
    assert node is not None
    assert node.value == expected


def test_returns_none_when_k_too_large(problem_module, node_cls):
    assert call_kth(problem_module, node_cls, [10, 20, 30], 4) is None


@pytest.mark.parametrize("invalid_k", [0, -1, -5])
def test_invalid_k_raises(problem_module, node_cls, invalid_k):
    with pytest.raises(ValueError):
        call_kth(problem_module, node_cls, [1, 2, 3], invalid_k)


def test_single_element(problem_module, node_cls):
    node = call_kth(problem_module, node_cls, [42], 1)
    assert node is not None
    assert node.value == 42


def test_structure_intact(problem_module, node_cls):
    head = build_linked_list([1, 2, 3, 4], node_cls)
    func = getattr(problem_module, FUNCTION_NAME)
    result = func(head, 2)
    # Ensure we can traverse from the returned node to the tail without issues
    assert list_from_node(result) == [3, 4]
