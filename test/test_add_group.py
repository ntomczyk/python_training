# -*- coding: utf-8 -*-

from model.group import Group

def test_adding_group(app):
    app.group.open_groups_page()
    app.group.create(Group(group_name="group1", header="header1", footer="footer2"))
    app.group.return_to_groups_page()

def test_adding_empty_group(app):
    app.group.open_groups_page()
    app.group.create(Group(group_name="", header="", footer=""))
    app.group.return_to_groups_page()
