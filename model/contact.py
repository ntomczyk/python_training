from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, photo=None, title=None, company=None, address=None, home_number=None, mobile_number=None,
                work_number=None, fax_number=None, email=None, email2=None, email3=None, home_page=None, birthday=None, birthmonth=None, birthyear=None, annday=None, annmonth=None, annyear=None, address2=None,
                 phone2=None, notes=None, id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.fax_number = fax_number
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.home_page = home_page
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear
        self.annday = annday
        self.annmonth = annmonth
        self.annyear = annyear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.firstname, self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(ct):
        if ct.id:
            return int(ct.id)
        else:
            return maxsize

