# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters +string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_digits(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
                    nickname=random_string("nickname", 20), title=random_string("title", 20), company=random_string("company", 20), address=random_string("address", 20),
                    home_number=random_digits("home_number", 20),  mobile_number=random_digits("mobile_number", 20),  work_number=random_digits("work_number", 20),  fax_number=random_digits("fax_number", 20),
                    email=random_string("email", 20), email2=random_string("email2", 20), home_page=random_string("home_page", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact",testdata, ids=[repr(x) for x in testdata])
def test_adding_contact_random(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()


#def test_adding_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = (Contact(firstname="Ada", lastname="Test", nickname="AdaTest_nickname", photo="/home/nina/Pulpit/cookie_monster.jpg",
#                                    title="Miss", company="TestCompany",address="Test street 26\n41-400 Warsaw", home_number="+4823233242",
#                                    mobile_number="+48666333666", work_number="+48222333222", fax_number="+48222444222", email="fake_mail1@gmail.com",
#                                    email2="fake_mail2@gmail.com", email3="fake_mail3@gmail.com", home_page="https://onet.pl", birthday="8",
#                                    birthmonth="March", birthyear="1980", annday="1", annmonth="January", annyear="2000",
#                                    address2="Flower street 22\n41-400 Warsaw", phone2="+48555333221", notes="Notestest1"))
#    app.contact.create_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == app.contact.count()
