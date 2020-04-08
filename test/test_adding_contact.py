# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_adding_contact(app):
    app.open_home_page()
    app.login( username = "secret", password = "admin")
    app.create_contact( Contact(firstname="Ada", lastname="Test", nickname="AdaTest_nickname", photo="/home/nina/Pulpit/cookie_monster.jpg",
                                    title="Miss", company="TestCompany",address="Test street 26\n41-400 Warsaw", home_number="+48 23233242",
                                    mobile_number="+48 666333666", work_number="+48 222333222", fax_number="+48 222444222", email="fake_mail1@gmail.com",
                                    email2="fake_mail2@gmail.com", email3="fake_mail3@gmail.com", home_page="https://onet.pl", birthday="8",
                                    birthmonth="March", birthyear="1980", annday="1", annmonth="January", annyear="2000",
                                    address2="Flower street 22\n41-400 Warsaw", phone2="+48 555333221", notes="Notestest1"))