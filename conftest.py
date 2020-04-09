import pytest
from fixture.application import Application


#@pytest.fixture(scope ="session") - it's not working correctly, after every test logout is not execute
@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture