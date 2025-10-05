from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


MODULE_NAME = "ch03_3_1_problem"
CLASS_NAME = "TripleStack"
VALID_INDICES = (0, 1, 2)


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


@pytest.fixture()
def triple_stack_cls(problem_module):
    assert hasattr(problem_module, CLASS_NAME), "Define a TripleStack class in problem.py"
    return getattr(problem_module, CLASS_NAME)


def make_stack(triple_stack_cls, capacity=3):
    return triple_stack_cls(capacity)


def test_push_and_pop_on_each_stack(triple_stack_cls):
    stack = make_stack(triple_stack_cls, capacity=4)
    for idx, items in enumerate([[1, 2], ["a"], [True, False, None]]):
        for item in items:
            stack.push(idx, item)
    assert stack.pop(0) == 2
    assert stack.pop(0) == 1
    assert stack.pop(1) == "a"
    assert stack.pop(2) is None
    assert stack.pop(2) is False
    assert stack.pop(2) is True


def test_peek_does_not_remove(triple_stack_cls):
    stack = make_stack(triple_stack_cls, capacity=2)
    stack.push(0, "first")
    stack.push(0, "second")
    assert stack.peek(0) == "second"
    assert stack.peek(0) == "second"
    assert stack.pop(0) == "second"
    assert stack.pop(0) == "first"


def test_is_empty_flags_correctly(triple_stack_cls):
    stack = make_stack(triple_stack_cls)
    for idx in VALID_INDICES:
        assert stack.is_empty(idx)
        stack.push(idx, idx)
        assert not stack.is_empty(idx)
        stack.pop(idx)
        assert stack.is_empty(idx)


def test_capacity_enforced(triple_stack_cls):
    stack = make_stack(triple_stack_cls, capacity=1)
    stack.push(1, "value")
    with pytest.raises(IndexError):
        stack.push(1, "overflow")


@pytest.mark.parametrize("index", [-1, 3, 99])
def test_invalid_index_raises(triple_stack_cls, index):
    stack = make_stack(triple_stack_cls)
    with pytest.raises(IndexError):
        stack.push(index, "oops")
    with pytest.raises(IndexError):
        stack.pop(index)
    with pytest.raises(IndexError):
        stack.peek(index)
    with pytest.raises(IndexError):
        stack.is_empty(index)


def test_pop_empty_stack_raises(triple_stack_cls):
    stack = make_stack(triple_stack_cls)
    with pytest.raises(IndexError):
        stack.pop(0)
