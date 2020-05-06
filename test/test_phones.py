import re
from random import randrange

def test_first_phone_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_phone_page(contact_from_edit_page)


def test_first_phone_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_view_page.home_number) == clear(contact_from_edit_page.home_number)
    assert clear(contact_from_view_page.work_number) == clear(contact_from_edit_page.work_number)
    assert clear(contact_from_view_page.mobile_number) == clear(contact_from_edit_page.mobile_number)
    assert clear(contact_from_view_page.phone2) == clear(contact_from_edit_page.phone2)


def test_phones_on_home_page_by_index(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_phone_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() - +]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x:x is not None,
                                                           [contact.home_number, contact.mobile_number, contact.work_number, contact.phone2]))))



