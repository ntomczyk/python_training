# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import unittest, time, re

class AddingContact(unittest.TestCase):
    def setUp(wd):
        wd.driver = webdriver.Firefox()
        wd.driver.implicitly_wait(30)

    
    def test_adding_contact(self):
        wd = self.driver
        self.open_home_page(wd)
        self.login(wd, username = "secret", password = "admin")
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys("Ada")
        wd.find_element_by_name("lastname").send_keys("Test")
        wd.find_element_by_name("nickname").send_keys("AdaTest_nickname")
       # wd.find_element_by_name("photo").send_keys("C:\\fakepath\\cookie_monster.jpg")
        wd.find_element_by_name("title").send_keys("Miss")
        wd.find_element_by_name("company").send_keys("TestCompany")
        wd.find_element_by_name("address").send_keys("Test street 26\n41-400 Warsaw")
        wd.find_element_by_name("home").send_keys("+48 23233242")
        wd.find_element_by_name("mobile").send_keys("+48 666333666")
        wd.find_element_by_name("work").send_keys("+48 222333222")
        wd.find_element_by_name("fax").send_keys("+48 222444222")
        wd.find_element_by_name("email").send_keys("fake_mail1@gmail.com")
        wd.find_element_by_name("email2").send_keys("fake_mail2@gmail.com")
        wd.find_element_by_name("email3").send_keys("fake_mail3@gmail.com")
        wd.find_element_by_name("email").send_keys("test_fake_mail1@gmail.com")
        wd.find_element_by_name("email2").send_keys("test_fake_mail2@gmail.com")
        wd.find_element_by_name("email3").send_keys("test_fake_mail3@gmail.com")
        wd.find_element_by_name("homepage").send_keys("https://onet.pl")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("8")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("March")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").send_keys("1980")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("address2").send_keys("Flower street 22\n41-400 Warsaw")
        wd.find_element_by_name("phone2").send_keys("home")
        wd.find_element_by_name("notes").send_keys("Notestest1")
        wd.find_element_by_name("phone2").send_keys("+48 555333221")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("pass").send_keys(username)
        wd.find_element_by_name("user").send_keys(password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
