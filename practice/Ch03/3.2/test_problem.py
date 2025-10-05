from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


MODULE_NAME = "ch03_3_2_problem"
CLASS_NAME = "MinStack"


def _load_problem_module():
    module_path = Path(__file__).with_name("problem.py")
    spec = importlib.util.spec_from_file_location(MODULE_NAME, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def min_stack_cls():
    module = _load_problem_module()
    assert hasattr(module, CLASS_NAME), "Define MinStack in problem.py"
    return getattr(module, CLASS_NAME)


@pytest.fixture()
def stack(min_stack_cls):
    return min_stack_cls()


def test_push_pop_peek(stack):
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        stack.peek()


def test_min_updates(stack):
    stack.push(5)
    stack.push(3)
    stack.push(7)
    assert stack.get_min() == 3
    stack.push(1)
    assert stack.get_min() == 1
    stack.pop()
    assert stack.get_min() == 3


def test_min_with_duplicates(stack):
    stack.push(2)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(1)
    assert stack.get_min() == 1
    stack.pop()
    assert stack.get_min() == 1
    stack.pop()
    assert stack.get_min() == 2


def test_get_min_on_empty_raises(min_stack_cls):
    stack = min_stack_cls()
    with pytest.raises(IndexError):
        stack.get_min()


def test_mixed_operations(stack):
    stack.push(4)
    stack.push(6)
    stack.push(5)
    stack.pop()
    stack.push(3)
    stack.push(7)
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == 4
