# -*- coding: utf-8 -*-

from model.group import Group

def test_adding_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(group_name="group1", header="header1", footer="footer2"))
    app.group.return_to_groups_page()
    app.session.logout()

def test_adding_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(group_name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()
