# -*- coding: utf-8 -*-
from model.contact import Contact



def test_adding_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname="Ada", lastname="Test", nickname="AdaTest_nickname", photo="/home/nina/Pulpit/cookie_monster.jpg",
                                    title="Miss", company="TestCompany",address="Test street 26\n41-400 Warsaw", home_number="+4823233242",
                                    mobile_number="+48666333666", work_number="+48222333222", fax_number="+48222444222", email="fake_mail1@gmail.com",
                                    email2="fake_mail2@gmail.com", email3="fake_mail3@gmail.com", home_page="https://onet.pl", birthday="8",
                                    birthmonth="March", birthyear="1980", annday="1", annmonth="January", annyear="2000",
                                    address2="Flower street 22\n41-400 Warsaw", phone2="+48555333221", notes="Notestest1"))
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
