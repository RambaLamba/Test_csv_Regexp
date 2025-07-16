import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  del contacts_list[0]

length_contacts_list = len(contacts_list)

def get_phone_number(person):
    pattern = r"(\+7|8)?([\s-])?(\()?(\d{3})(\))?([\s-])?(\d{3})([\s-])?(\d{2})[\s-]*(\d{2})((\s)(\()?(доб.|доб.)(\s(\d{4})))?"
    replace = r"+7(\4)\7-\9-\10 \14\16"
    # result = re.sub(pattern, replace, ", ".join(person))
    # print(result)
    # number = re.findall(pattern, " ".join(person))
    # print(number)

    result = re.finditer(pattern, ", ".join(person))
    for r in result:
        # print(r.group())
        number = re.sub(pattern, replace, r.group())
        print(number)

def get_full_name():
    for name in contacts_list:
        # print(" ".join(name))
        full_name = name[:2]
        join_full_name = " ".join(full_name)
        print(" ".join(full_name))
        get_phone_number(name)


if __name__ == '__main__':
    get_full_name()

