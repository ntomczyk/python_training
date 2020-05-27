from model.group import Group
from random import randrange
import random


def test_editing_group_name(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="groupone", header="headerone", footer="footerone"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.update_group_by_id(group.id,Group(header="headertwo"))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),key=Group.id_or_max)

# def test_editing_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="groupone", header="headerone", footer="footerone"))
#     old_groups = app.group.get_group_list()
#     app.group.update_first_group(Group(header="headertwo"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)