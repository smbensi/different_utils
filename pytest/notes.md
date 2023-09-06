pytest : tool that allows to write **unitest**


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