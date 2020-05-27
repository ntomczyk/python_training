# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group_ddd(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),key=Group.id_or_max)


#def test_add_group_ddd(app, json_groups):
#    group = json_groups
#    old_groups = app.group.get_group_list()
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == app.group.count()
#    old_groups.append(group)
#   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_adding_group(app):
    #old_groups = app.group.get_group_list()
    #group = (Group(name="group10", header="header1", footer="footer2"))
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == app.group.count()
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_adding_empty_group(app):
    #old_groups = app.group.get_group_list()
    #group = (Group(name="", header="", footer=""))
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
