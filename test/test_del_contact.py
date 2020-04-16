from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Monika", lastname="Deletetest"))
    app.contact.delete_first_contact()
