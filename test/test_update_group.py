from model.group import Group
from random import randrange


def test_editing_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="groupone", header="headerone", footer="footerone"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = (Group(group_name="grouptwo"))
    group.id = old_groups[index].id
    app.group.update_group_by_index(index,group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_editing_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="groupone", header="headerone", footer="footerone"))
    old_groups = app.group.get_group_list()
    app.group.update_first_group(Group(header="headertwo"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)