import ast

import pytest

from flake8_printf_formatting import Plugin


@pytest.fixture
def results():
    def _results(string):
        return ["{}:{}: {}".format(*r) for r in Plugin(ast.parse(string)).run()]

    return _results


@pytest.mark.parametrize(
    "code",
    [
        # Test strings
        "print('foo %s' % 'bar')",
        # Test bytes
        "print(b'foo %s' % b'bar')",
    ],
)
def test_complain_simple_expressions(results, code):
    expected_message = "1:6: MOD001 do not use printf-style string formatting"
    assert results(code) == [expected_message]


def test_complain_nested_expressions(results):
    expected_messages = [
        "1:6: MOD001 do not use printf-style string formatting",
        "1:18: MOD001 do not use printf-style string formatting",
    ]
    assert results("print('foo %s' % ('bar %s' % 'baz'))") == expected_messages


@pytest.mark.parametrize(
    "code",
    [
        # Test an empty string
        "",
        # Test str.format
        "print('foo {}'.format('bar'))",
        # Test a simple term
        "42 % 10",
        # Test augmented assignment
        "foo = 42; foo %= 10",
    ],
)
def test_ignore_other_expressions(results, code):
    assert not results(code)
