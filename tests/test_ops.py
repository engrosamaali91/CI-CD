import math
from mymath.ops import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6

def test_mul():
    assert mul(3, 7) == 21

def test_div():
    assert div(8, 2) == 4

def test_div_by_zero():
    import pytest   
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_float_sanity():
    # use math.isclose for floats.
    assert math.isclose(add(0.1, 0.2), 0.3, rel_tol=1e-9, abs_tol=1e-12)
