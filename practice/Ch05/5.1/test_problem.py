from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


MODULE_NAME = "ch05_5_1_problem"
FUNCTION_NAME = "insert_bits"


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
def insert_bits(problem_module):
    assert hasattr(problem_module, FUNCTION_NAME), "Define insert_bits in problem.py"
    return getattr(problem_module, FUNCTION_NAME)


def test_book_example(insert_bits):
    target = int("10000000000", 2)
    source = int("10011", 2)
    result = insert_bits(target, source, 2, 6)
    assert result == int("10001001100", 2)


def test_overwrite_middle_zeroes(insert_bits):
    target = int("111111", 2)
    source = int("00", 2)
    result = insert_bits(target, source, 2, 3)
    assert result == int("110011", 2)


def test_replace_entire_number(insert_bits):
    target = int("0", 2)
    source = int("10101", 2)
    result = insert_bits(target, source, 0, 4)
    assert result == source


def test_single_bit_replacement(insert_bits):
    target = int("1010", 2)
    source = 1
    result = insert_bits(target, source, 1, 1)
    assert result == int("1110", 2)


def test_invalid_indices(insert_bits):
    with pytest.raises(ValueError):
        insert_bits(0, 1, 5, 3)
    with pytest.raises(ValueError):
        insert_bits(0, 1, -1, 3)
    with pytest.raises(ValueError):
        insert_bits(0, 1, 0, -1)


def test_source_not_fitting(insert_bits):
    target = 0
    source = int("111", 2)
    with pytest.raises(ValueError):
        insert_bits(target, source, 0, 1)
