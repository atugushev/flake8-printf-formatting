[![PyPI version](https://img.shields.io/pypi/v/flake8-printf-formatting.svg)](https://pypi.org/project/flake8-printf-formatting/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/flake8-printf-formatting.svg)](https://pypi.org/project/flake8-printf-formatting/)
[![Build status](https://img.shields.io/travis/atugushev/flake8-printf-formatting/master.svg?logo=travis)](https://travis-ci.org/atugushev/flake8-printf-formatting)
[![Coverage](https://codecov.io/gh/atugushev/flake8-printf-formatting/branch/master/graph/badge.svg)](https://codecov.io/gh/atugushev/flake8-printf-formatting)

flake8-printf-formatting
========================

flake8 plugin which forbids printf-style string formatting

## Installation

`pip install flake8-printf-formatting`

## Codes

| Code   | Description                               |
|--------|-------------------------------------------|
| MOD001 | do not use printf-style string formatting |

## Rationale

The official Python 3 documentation [doesn't recommend](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)
printf-style string formatting:

> The formatting operations described here exhibit a variety of quirks that
> lead to a number of common errors (such as failing to display tuples and
> dictionaries correctly). Using the newer formatted string literals,
> the `str.format` interface, or template strings may help avoid these errors.
> Each of these alternatives provides their own trade-offs and benefits of simplicity,
> flexibility, and/or extensibility.

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.8
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-printf-formatting]
```
