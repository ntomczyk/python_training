from model.group import Group


def test_editing_group_name(app):
    app.group.open_groups_page()
    app.group.create(Group(group_name="groupone", header="headerone", footer="footerone"))
    app.group.update_first_group(Group(group_name="grouptwo"))

def test_editing_group_header(app):
    app.group.open_groups_page()
    app.group.create(Group(group_name="groupone", header="headerone", footer="footerone"))
    app.group.update_first_group(Group( header="headertwo"))