import sys

import pytest


@pytest.mark.skip
def test_first():
    a = 33
    b = 44
    result = a+b
    assert result == 77


def test_second():
    a = 33
    b = 44
    result = a + b
    assert result == 88

@pytest.mark.skipif(sys.version_info > (3,8), reason="version not supported")
def test_third():
    print(sys.version_info)
    a = 33
    b = 44
    result = a+b
    assert result < 78


@pytest.mark.xfail
def test_check_in():
    name = "Vaishnavi"
    fullName = "Vaishnavi Sachin Gore"
    assert name in fullName


@pytest.mark.xfail
def test_check_is():
    name = "Vaishnavi"
    fullName = "Vaishnavi Sachin Gore"
    assert name is fullName


@pytest.mark.parametrize("username, password",
                         [
                             ("user", "pass"),
                             ("vaishnavi", "vai@123"),
                             ("vaishnavik", "vaik@123")
                         ])
def test_login(username, password):
    print(username+' '+password)

