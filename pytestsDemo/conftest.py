import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["yui","morii","yuimoriidesign.com"]


@pytest.fixture(params=[("chrome","yui","morii"), ("Firefox","morii"), ("IE","SS")])
def crossBrowser(request):
    return request.param


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
