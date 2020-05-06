from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact
import re

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
        self.contact_cache = None

    def update_first_contact(self, edit_data):
        wd = self.app.wd
        self.find_first_contact()
        self.fill_contact_form(edit_data)
        # Update contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def update_contact_by_index(self, index, edit_data):
        wd = self.app.wd
        self.app.open_home_page
        self.find_contact_by_index(index)
        self.fill_contact_form(edit_data)
        # Update contact
        wd.find_element_by_name("update").click()
        self.app.open_home_page
        self.contact_cache = None

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

    def change_photo(self, field_name, photo):
        wd = self.app.wd
        if photo is not None:
            wd.find_element_by_name(field_name).send_keys(photo)

    def fill_contact_form(self, contact):
        wd = self.app.wd

        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # Add picture
        self.change_photo("photo", contact.photo)
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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        self.find_contact_by_index(index)
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.open_home_page()
        self.contact_cache = None

    def find_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def find_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells= row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                if len(all_phones) < 4:
                    continue;
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id = id, home_number=all_phones[0], mobile_number=all_phones[1], work_number=all_phones[2],
                     phone2=all_phones[3]))
        return (self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_number=home_number, work_number=work_number,
                       mobile_number=mobile_number, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H:(.*)", text).group(1)
        work_number = re.search("W:(.*)", text).group(1)
        mobile_number = re.search("M:(.*)", text).group(1)
        phone2 = re.search("P:(.*)", text).group(1)
        return Contact( home_number=home_number, work_number=work_number,
                       mobile_number=mobile_number, phone2=phone2)




