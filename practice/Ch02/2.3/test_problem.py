from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Iterable

import pytest


MODULE_NAME = "ch02_2_3_problem"
NODE_CLASS_NAME = "Node"
FUNCTION_NAME = "delete_middle_node"


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
def delete_middle_node(problem_module):
    assert hasattr(problem_module, FUNCTION_NAME), "Define delete_middle_node in problem.py"
    return getattr(problem_module, FUNCTION_NAME)


def build_list(values: Iterable, node_cls):
    head = None
    prev = None
    nodes = []
    for value in values:
        node = node_cls(value)
        nodes.append(node)
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head, nodes


def list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


def test_delete_middle_node_removes_value(node_cls, delete_middle_node):
    head, nodes = build_list([1, 2, 3, 4, 5], node_cls)
    delete_middle_node(nodes[2])  # delete value 3
    assert list_values(head) == [1, 2, 4, 5]
    # Ensure the node reference now carries the next value (since list mutated in place)
    assert nodes[2].value == 4


def test_delete_first_not_allowed(node_cls, delete_middle_node):
    head, nodes = build_list(["a", "b", "c"], node_cls)
    with pytest.raises(ValueError):
        delete_middle_node(nodes[0])
    assert list_values(head) == ["a", "b", "c"]


def test_delete_last_not_allowed(node_cls, delete_middle_node):
    head, nodes = build_list([10, 20, 30], node_cls)
    with pytest.raises(ValueError):
        delete_middle_node(nodes[-1])
    assert list_values(head) == [10, 20, 30]


def test_delete_none_raises(delete_middle_node):
    with pytest.raises(ValueError):
        delete_middle_node(None)


def test_multiple_middle_deletions(node_cls, delete_middle_node):
    head, nodes = build_list(["start", "mid1", "mid2", "end"], node_cls)
    delete_middle_node(nodes[1])  # remove "mid1"
    # Need to capture new list structure to delete new middle (original mid2 now at nodes[2])
    delete_middle_node(nodes[2])  # original "mid2" node now second from end
    assert list_values(head) == ["start", "end"]
