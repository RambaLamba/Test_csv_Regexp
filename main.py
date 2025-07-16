from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  del contacts_list[0]
pprint(contacts_list)

length_contacts_list = len(contacts_list)


def get_phone_number(person):
    pattern = ""
    number = re.split(pattern, person)
    return number


# def get_full_name():
#     for name in contacts_list:
#         full_name = name[:2]
#         join_full_name = " ".join(full_name)
#         print(" ".join(full_name))

# get_full_name()

