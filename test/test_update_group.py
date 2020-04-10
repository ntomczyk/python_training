from model.group import Group


def test_editing_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(group_name="groupone", header="headerone", footer="footerone"))
    app.group.update_first_group(Group(group_name="grouptwo", header="headertwo", footer="footertwo"))
    app.session.logout()