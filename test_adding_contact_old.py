# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from contact import Contact

import unittest, time, re

class AddingContact(unittest.TestCase):
    def setUp(wd):
        wd.driver = webdriver.Firefox()
        wd.driver.implicitly_wait(30)

    
    def test_adding_contact(self):
        wd = self.driver
        self.open_home_page()
        self.login( username = "secret", password = "admin")
        self.create_contact( Contact(firstname="Ada", lastname="Test", nickname="AdaTest_nickname", photo="/home/nina/Pulpit/cookie_monster.jpg",
                                        title="Miss", company="TestCompany",address="Test street 26\n41-400 Warsaw", home_number="+48 23233242",
                                        mobile_number="+48 666333666", work_number="+48 222333222", fax_number="+48 222444222", email="fake_mail1@gmail.com",
                                        email2="fake_mail2@gmail.com", email3="fake_mail3@gmail.com", home_page="https://onet.pl", birthday="8",
                                        birthmonth="March", birthyear="1980", annday="1", annmonth="January", annyear="2000",
                                        address2="Flower street 22\n41-400 Warsaw", phone2="+48 555333221", notes="Notestest1"))
        self.logout()


    def open_home_page(self):
        wd = self.driver
        wd.get("http://localhost/addressbook/index.php")


    def login(self,username, password):
        wd = self.driver
        wd.find_element_by_name("pass").send_keys(username)
        wd.find_element_by_name("user").send_keys(password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def create_contact(self, contact):
        wd = self.driver
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        # Fill in new contact form
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Add picture
        wd.find_element_by_name("photo").send_keys(contact.photo)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home_number)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_name("work").send_keys(contact.work_number)
        wd.find_element_by_name("fax").send_keys(contact.fax_number)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.home_page)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthmonth)
        wd.find_element_by_name("byear").send_keys(contact.birthyear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.annday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.annmonth)
        wd.find_element_by_name("ayear").send_keys(contact.annyear)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # Submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def logout(self):
        wd = self.driver
        wd.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
