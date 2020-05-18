from fixture.contact import *
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 10
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
                    nickname=random_string("nickname", 20), title=random_string("title", 20),
                    company=random_string("company", 20), address=random_string("address", 20),
                    home_number=random_digits("home_number", 20), mobile_number=random_digits("mobile_number", 20),
                    work_number=random_digits("work_number", 20), fax_number=random_digits("fax_number", 20),
                    email=random_string("email", 20), email2=random_string("email2", 20),
                    home_page=random_string("home_page", 20))
            for i in range(5)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))