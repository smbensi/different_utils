# pytest : tool that allows to write **unitests**

[github source](https://github.com/koaning/blackjack/)

install pytest:
> python -m pip install pytest

creat file : `test_function.py`
```python
def test_simple():
    assert foo(*args) == CONST
```

then
> pytest test_function.py

pytest is able to find alone the test files by finding function and files containing the word "test" and you can run only
> pytest

**you need one function per test**

to get more detailed test results
> pytest --verbose

You can specify a unit function
> pytest test_func.py::test_simple


you can put everything in one function by decorating with

```python
import pytest

from blackjack import card_score

@pytest.mark.parametrize("cards,score", [('JK', 20), ('KKK', 0), ('AA', 12), ('AK', 21)])
def test_simple_usecase(cards, score):
    assert card_score(cards) == score
```

You can create a test folder with a \_\_init__.py file

pytest gives a context manager
```python 
def test_raise_error():
    with pytest.raises(ValueError):
        card_score("")
```

# pytest-cov package for coverage

run
> pytest --cov blackjack

can show how many of the lines of code have been tested during the 
tests

You can have a longer report with this instruction
> pytest --cov blackjack --cov-report html

You should see a new htmlcov folder that contains the index.html file that gives you the drilldown.

# Git

you can run the tests on every pull or push with a particular config file

```yaml
# .github/workflows/pythonpackage.yml
name: Python package

on: [push, pull_request]

jobs:
build:
  runs-on: ubuntu-latest
  strategy:
  matrix:
      python-version: [3.7]

  steps:
  - uses: actions/checkout@v2
  - name: Set up Python ${{ matrix.python-version }}
  uses: actions/setup-python@v1
  with:
      python-version: ${{ matrix.python-version }}
  - name: Test with pytest
  run: |
      pip install pytest
      pytest --verbose
```