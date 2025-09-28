from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


MODULE_NAME = "ch04_4_1_problem"
FUNCTION_NAME = "route_exists"


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
def route_exists(problem_module):
    assert hasattr(problem_module, FUNCTION_NAME), "Define route_exists in problem.py"
    return getattr(problem_module, FUNCTION_NAME)


GRAPH = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": [],
    "E": [],
}


def test_reachable_path(route_exists):
    assert route_exists(GRAPH, "A", "E") is True


def test_no_path(route_exists):
    assert route_exists(GRAPH, "C", "D") is False


def test_start_equals_end(route_exists):
    assert route_exists(GRAPH, "B", "B") is True


def test_cycle_graph(route_exists):
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [],
    }
    assert route_exists(graph, 1, 3) is True
    assert route_exists(graph, 3, 4) is False


@pytest.mark.parametrize("start, end", [("X", "A"), ("A", "Z")])
def test_unknown_nodes_raise(route_exists, start, end):
    with pytest.raises(KeyError):
        route_exists(GRAPH, start, end)
