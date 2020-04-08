# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_adding_group(app):
    app.open_home_page()
    app.login( username = "secret", password = "admin")
    app.open_groups_page()
    app.create_group( Group(group_name ="group1", header ="header1", footer ="footer2"))
    app.return_to_groups_page()
    app.logout()

def test_adding_empty_group(app):
    app.open_home_page()
    app.login( username="secret", password="admin")
    app.open_groups_page()
    app.create_group( Group(group_name="", header="", footer=""))
    app.return_to_groups_page()
    app.logout()


