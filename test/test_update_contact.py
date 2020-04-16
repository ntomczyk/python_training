from model.contact import Contact

def test_update_first_contact(app):
    app.contact.update_first_contact( Contact(firstname="Adam", lastname="Testum",notes="Notestest2"))