from goodhello import hello, bye, greet
import runpy
import pytest


def test_hello_returns_none():
    assert hello() is None


def test_bye_returns_none():
    assert bye() is None


def test_greet_returns_none():
    assert greet() is None


def test_hello_prints_expected_text(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, DevOps learner!"


def test_bye_prints_expected_text(capsys):
    bye()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodbye!"


def test_greet_prints_expected_text(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Happy Weekend"


@pytest.mark.parametrize(
    "func,expected",
    [
        (hello, "Hello, DevOps learner!"),
        (bye, "Goodbye!"),
        (greet, "Happy Weekend"),
    ],
)
def test_prints_expected_text_param(func, capsys, expected):
    func()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


def test_functions_do_not_raise():
    # Simply calling the functions should not raise
    hello()
    bye()
    greet()


def test_docstrings_present():
    assert isinstance(hello.__doc__, str) and hello.__doc__.strip()
    assert isinstance(bye.__doc__, str) and bye.__doc__.strip()
    assert isinstance(greet.__doc__, str) and greet.__doc__.strip()


def test_module_run_prints_both_greetings(capsys):
    runpy.run_module("goodhello", run_name="__main__")
    out = capsys.readouterr().out.strip().splitlines()
    assert out == ["Hello, DevOps learner!", "Goodbye!"]
