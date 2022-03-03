##########################
# Optimalize tests
##########################
import math_func
import pytest

# 1. Basic
def test_add():
    assert math_func.add(7, 3) == 10

def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'

def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36

# 2. You can connect them to 1 function
def test_add():
    assert math_func.add(7, 3) == 10
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    result = math_func.add(10.5, 25.5)
    assert result == 36

# 3. You can parametrize function
@pytest.mark.parametrize('x, y, result',
                        [
                            (7, 3, 10),
                            ('Hello', ' World', 'Hello World'),
                            (10.5, 25.5, 36),
                        ]
                        )
def test_add(x, y, result):
    assert math_func.add(x, y) == result
