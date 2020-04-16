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
        self.find_first_contact()
        self.fill_contact_form(edit_data)
        # Update contact
        wd.find_element_by_name("update").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd

        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # Add picture
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_number)
        self.change_field_value("mobile", contact.mobile_number)
        self.change_field_value("work", contact.work_number)
        self.change_field_value("fax", contact.fax_number)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.home_page)
        self.change_dropdown_value("bday", contact.birthday)
        self.change_dropdown_value("bmonth", contact.birthmonth)
        self.change_field_value("byear", contact.birthyear)
        self.change_dropdown_value("aday", contact.annday)
        self.change_dropdown_value("amonth", contact.annmonth)
        self.change_field_value("ayear", contact.annyear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        self.find_first_contact()
        # delete contact
        wd.find_element_by_xpath('//input[@value="Delete"]').click()

    def find_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
