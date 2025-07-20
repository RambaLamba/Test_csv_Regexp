import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def format_phone(phone):
    """Приводит номер телефона к формату [+7(999)999-99-99]"""
    if not phone:
        return ""

    pattern = (r"(\+7|8)?([\s-])?(\()?(\d{3})(\))?([\s-])?(\d{3})([\s-])?"
               r"(\d{2})[\s-]*(\d{2})((\s)(\()?(доб.|доб.)(\s(\d{4})))?")
    replace = r"+7(\4)\7-\9-\10 \14\16"
    formated_number = re.sub(pattern, replace, phone)
    return formated_number.strip()

for contact in contacts_list[1:]:
    full_name = " ".join(contact[:3]).split()
    contact[0] = full_name[0] if len(full_name) > 0 else ""
    contact[1] = full_name[1] if len(full_name) > 1 else ""
    contact[2] = full_name[2] if len(full_name) > 2 else ""

merged_contacts = {}
for contact in contacts_list[1:]:
    key = (contact[0], contact[1])
    if key not in merged_contacts:
        merged_contacts[key] = contact
    else:
        existing = merged_contacts[key]
        for i in range(len(contact)):
            if not existing[i] and contact[i]:
                existing[i] = contact[i]

for contact in merged_contacts.values():
    if contact[5]:
        contact[5] = format_phone(contact[5])

header = contacts_list[0]
result = [header] + list(merged_contacts.values())

with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(result)