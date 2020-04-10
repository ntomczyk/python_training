from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        # Fill in new contact form
        self.fill_contact_form(contact)
        # Submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def update_first_contact(self, edit_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(edit_data)
        # Update contact
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
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

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # delete contact
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
