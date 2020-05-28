from model.contact import Contact


def test_compare_contacts(app,db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)


    def merge_emails_like_on_home_page(contacts_from_db):
        return "\n".join(filter(lambda x: x != "" and x is not None,
                                map(lambda x: x.strip(), [contacts_from_db.email, contacts_from_db.email2])))

    def merge_phones_like_on_home_page(contacts_from_db):
        return "\n".join(filter(lambda x: x != "" and x is not None,
                                map(lambda x: x.strip(), [contacts_from_db.home_number, contacts_from_db.mobile_number, contacts_from_db.work_number])))


    for x, y in zip(sorted(contacts_from_home_page, key=Contact.id_or_max), sorted(contacts_from_db, key=Contact.id_or_max)):
        assert x.firstname == y.firstname
        assert x.lastname ==y.lastname
        assert x.address == y.address
        assert (x.all_emails_from_home_page) == (merge_emails_like_on_home_page(y))
        assert (x.all_phones_from_home_page) == (merge_phones_like_on_home_page(y))
