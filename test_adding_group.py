# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class AddingGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_adding_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "secret", password = "admin")
        self.open_groups_page(wd)
        self.create_group(wd, Group(group_name ="group1", header ="header1", footer ="footer2"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_adding_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="secret", password="admin")
        self.open_groups_page(wd)
        self.create_group(wd, Group(group_name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)


    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")


    def login(self, wd, username, password):
        wd.find_element_by_name("pass").send_keys(username)
        wd.find_element_by_name("user").send_keys(password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()


    def create_group(self, wd, group):
        # Add new group
        wd.find_element_by_name("new").click()
        # Fill in group form
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit groups creation
        wd.find_element_by_name("submit").click()


    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
