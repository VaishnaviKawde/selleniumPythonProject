import pytest

@pytest.mark.smoke
def test_first():
    a = 10
    b = 20
    assert a == b


@pytest.mark.regression
def test_2nd():
    a = 10
    b = 20
    assert a < b


@pytest.mark.smoke
@pytest.mark.regression
def test_3rd():
    a = 10
    b = 20
    assert a > b


@pytest.mark.vaishnavi
def test_fourth():
    a = 10
    b = 20
    res = a + b
    assert res == 30



