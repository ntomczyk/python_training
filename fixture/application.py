from selenium import webdriver
from selenium.webdriver.support.select import Select

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("pass").send_keys(username)
        wd.find_element_by_name("user").send_keys(password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        # Add new group
        wd.find_element_by_name("new").click()
        # Fill in group form
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit groups creation
        wd.find_element_by_name("submit").click()

    def create_contact(self, contact):
        wd = self.wd
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

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
