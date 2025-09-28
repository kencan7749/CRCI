from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


MODULE_NAME = "ch01_1_1_problem"
REQUIRED_FUNCTIONS = ("has_unique_chars", "has_unique_chars_no_extra")


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


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_required_functions_exist(func_name, problem_module):
    assert hasattr(problem_module, func_name), f"{func_name} is not defined in problem.py"


@pytest.mark.parametrize(
    "text",
    ["", "a", "abcdef", "AaBbCc", "0123456789", "かきくけこ"],
)
@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_unique_inputs(func_name, text, problem_module):
    func = getattr(problem_module, func_name)
    assert func(text) is True


@pytest.mark.parametrize(
    "text",
    ["aa", "aba", "Hello", "11234567890", "ミミ"],
)
@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_non_unique_inputs(func_name, text, problem_module):
    func = getattr(problem_module, func_name)
    assert func(text) is False


@pytest.mark.parametrize("func_name", REQUIRED_FUNCTIONS)
def test_long_input(func_name, problem_module):
    func = getattr(problem_module, func_name)
    unique_part = "".join(chr(32 + i) for i in range(60))
    assert func(unique_part) is True
    assert func(unique_part + "A") is False
