from model.contact import Contact
from random import randrange

def test_update_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Lena", lastname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = (Contact(firstname="Lenaupdate", lastname="Testum", notes="Notestest"))
    app.contact.update_contact_by_index(index,contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact

def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Lena", lastname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = ( Contact(firstname="Lenaupdate", lastname="Testum",notes="Notestest"))
    app.contact.update_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact

