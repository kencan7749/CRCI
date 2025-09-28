from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Iterable, List

import pytest


MODULE_NAME = "ch02_2_1_problem"
REQUIRED_FUNCTIONS = ("remove_duplicates", "remove_duplicates_no_buffer")
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


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_required_functions_exist(func_name, problem_module):
    assert hasattr(problem_module, func_name), f"{func_name} is not defined in problem.py"


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


def linked_list_to_list(head) -> List:
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_empty_list(func_name, problem_module, node_cls):
    func = getattr(problem_module, func_name)
    assert func(None) is None


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_removes_duplicates(func_name, problem_module, node_cls):
    func = getattr(problem_module, func_name)
    head = build_linked_list([1, 2, 3, 2, 1, 4, 3], node_cls)
    new_head = func(head)
    assert linked_list_to_list(new_head) == [1, 2, 3, 4]


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_all_duplicates(func_name, problem_module, node_cls):
    func = getattr(problem_module, func_name)
    head = build_linked_list(["a", "a", "a", "a"], node_cls)
    new_head = func(head)
    assert linked_list_to_list(new_head) == ["a"]


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_already_unique(func_name, problem_module, node_cls):
    func = getattr(problem_module, func_name)
    values = [1, 2, 3, 4]
    head = build_linked_list(values, node_cls)
    new_head = func(head)
    assert linked_list_to_list(new_head) == values


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_handles_strings(func_name, problem_module, node_cls):
    func = getattr(problem_module, func_name)
    head = build_linked_list(list("abaccadb"), node_cls)
    new_head = func(head)
    assert "".join(linked_list_to_list(new_head)) == "abcd"
