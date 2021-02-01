[![PyPI version](https://img.shields.io/pypi/v/flake8-printf-formatting.svg)](https://pypi.org/project/flake8-printf-formatting/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/flake8-printf-formatting.svg)](https://pypi.org/project/flake8-printf-formatting/)
![Tests](https://github.com/atugushev/flake8-printf-formatting/workflows/Tests/badge.svg)
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

### Bad

```python
print("Hello, %s!" % name)
```

### Good

```python
print("Hello, {name}!".format(name=name))
```

### Even better

```python
print(f"Hello, {name}!")
```

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

## Release process

1. Bump version in `setup.cfg`.
1. Add a commit "Release vX.Y.Z".
1. Make sure checks still pass.
1. [Draft a new release](https://github.com/atugushev/flake8-printf-formatting/releases/new) with a tag name "X.Y.Z" and describe changes which involved in the release.
1. Publish the release.
