from fixture.group import *
import random
import string

constant = [
    Group(group_name= "name1", header="header1", footer="footer1"),
    Group(group_name="name2", header="header2", footer="footer2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters +string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])



testdata =[Group(group_name= "", header="", footer="")]+\
          [Group(group_name= random_string("group_name", 10), header=random_string("header", 10), footer= random_string("footer", 10))
    for i in range(5)]