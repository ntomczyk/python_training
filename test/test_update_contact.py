from model.contact import Contact
from random import randrange
import random

def test_update_some_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Lena", lastname="Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #edit_data = (Contact(firstname="Lenaupdate", lastname="Testum", notes="Notestest"))
    print(contact.id)
    app.contact.update_contact_by_id(contact.id,(Contact(lastname="Testum", notes="Notestest")))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    #old_contacts[id] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

# def test_update_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create_contact(Contact(firstname="Lena", lastname="Test"))
#     old_contacts = app.contact.get_contact_list()
#     contact = ( Contact(firstname="Lenaupdate", lastname="Testum",notes="Notestest"))
#     app.contact.update_first_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact

