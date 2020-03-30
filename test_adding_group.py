# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddingGroup(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)

    
    def test_adding_group(self):
        wb = self.wb
        wb.get("http://localhost/addressbook/index.php")
        wb.find_element_by_name("pass").send_keys("secret")
        wb.find_element_by_name("user").send_keys("admin")
        wb.find_element_by_name("pass").click()
        wb.find_element_by_xpath("//input[@value='Login']").click()
        wb.find_element_by_link_text("groups").click()
        wb.find_element_by_name("new").click()
        wb.find_element_by_name("group_name").send_keys("test2")
        wb.find_element_by_name("group_header").send_keys("header")
        wb.find_element_by_name("group_footer").send_keys("footer")
        wb.find_element_by_name("submit").click()
        wb.find_element_by_link_text("group page").click()
        wb.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wb.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wb.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wb.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wb.quit()


if __name__ == "__main__":
    unittest.main()
