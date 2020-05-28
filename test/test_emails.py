import re
from random import randrange


def test_emails_on_home_page_by_index(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None,
                            map(lambda x: x.strip(), [contact.email, contact.email2, contact.email3])))