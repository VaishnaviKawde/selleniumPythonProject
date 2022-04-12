import pytest

@pytest.fixture
def setup():
    print("get driver")
    print("maximize window")
    yield
    print("print title")
    print("close window")


def test_1(setup):
    print("open url of facebook")


def test_2(setup):
    print("open url of gmail")


def test_3(setup):
    print("open url of amazon")

