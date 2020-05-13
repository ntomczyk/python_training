# -*- coding: utf-8 -*-

from model.group import Group
from fixture.group import *
import pytest
#from data.add_group import testdata
from data.add_group import constant as testdata


@pytest.mark.parametrize("group",testdata, ids=[repr(x) for x in testdata])
def test_add_group_ddd(app,group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == app.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_adding_group(app):
    #old_groups = app.group.get_group_list()
    #group = (Group(group_name="group10", header="header1", footer="footer2"))
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == app.group.count()
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_adding_empty_group(app):
    #old_groups = app.group.get_group_list()
    #group = (Group(group_name="", header="", footer=""))
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
