import ast

import pytest

from flake8_printf_formatting import Plugin

EXPECTED_MESSAGE = "1:6: MOD001 do not use printf-style string formatting"


@pytest.fixture
def results():
    def _results(string):
        return ["{}:{}: {}".format(*r) for r in Plugin(ast.parse(string)).run()]

    return _results


def test_str(results):
    assert results("print('foo %s' % ('bar',))") == [EXPECTED_MESSAGE]


def test_bytes(results):
    assert results("print(b'foo %s' % ('bar',))") == [EXPECTED_MESSAGE]


def test_empty_string(results):
    assert not results("")


def test_str_format(results):
    assert not results("print('foo {}'.format('bar'))")


def test_term(results):
    assert not results("42 % 10")


def test_augmented_assignment(results):
    assert not results("foo = 42; foo %= 10")
