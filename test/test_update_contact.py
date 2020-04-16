from model.contact import Contact

def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Lena", lastname="Test"))
    app.contact.update_first_contact( Contact(firstname="Lenaupdate", lastname="Testum",notes="Notestest"))