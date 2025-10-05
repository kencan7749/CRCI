from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


MODULE_NAME = "ch01_1_3_problem"
FUNCTION_NAME = "urlify"


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
def urlify(problem_module):
    assert hasattr(problem_module, FUNCTION_NAME), "Define urlify in problem.py"
    return getattr(problem_module, FUNCTION_NAME)


@pytest.mark.parametrize(
    "text, true_length, expected",
    [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("Hello World", 11, "Hello%20World"),
        ("NoSpaces", 8, "NoSpaces"),
        ("Trailing  spaces    ", 18, "Trailing%20%20spaces"),
        ("  Leading", 9, "%20%20Leading"),
    ],
)
def test_urlify_basic_cases(urlify, text, true_length, expected):
    assert urlify(text, true_length) == expected


@pytest.mark.parametrize("text, true_length", [("Short", -1), ("Short", 6)])
def test_invalid_true_length(urlify, text, true_length):
    with pytest.raises(ValueError):
        urlify(text, true_length)


def test_ignores_trailing_buffer(urlify):
    text = "Space end      "
    assert urlify(text, 9) == "Space%20end"
