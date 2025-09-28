from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


MODULE_NAME = "ch01_1_2_problem"
FUNCTION_NAME = "are_permutations"


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


def test_function_exists(problem_module):
    assert hasattr(problem_module, FUNCTION_NAME), "Define are_permutations in problem.py"


@pytest.mark.parametrize(
    "first, second",
    [
        ("", ""),
        ("abc", "bca"),
        ("aabbcc", "baccab"),
        ("123 45", " 54321"),
        ("ミカド", "カミド"),
    ],
)
def test_permutation_pairs(first, second, problem_module):
    func = getattr(problem_module, FUNCTION_NAME)
    assert func(first, second) is True
    assert func(second, first) is True


@pytest.mark.parametrize(
    "first, second",
    [
        ("abc", "ab"),
        ("abc", "abd"),
        ("abc", "abC"),
        ("hello", "hlelo!"),
        ("ミカド", "ミカドー"),
    ],
)
def test_non_permutation_pairs(first, second, problem_module):
    func = getattr(problem_module, FUNCTION_NAME)
    assert func(first, second) is False
    assert func(second, first) is False


@pytest.mark.parametrize("first, second", [("longinput", ""), ("aaaab", "baaac")])
def test_mismatched_counts(first, second, problem_module):
    func = getattr(problem_module, FUNCTION_NAME)
    assert func(first, second) is False
