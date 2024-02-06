import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


patern_tel = r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?'
patern_sub = r'+7(\2)\3-\4-\5\7\8\9'
list_for_telephone = []
for contact in contacts_list:
    contact[5] = re.sub(patern_tel, patern_sub, contact[5])
    list_for_telephone.append(contact)


info_list = []
for data in list_for_telephone:
    file = ' '.join(data[:3]).split()
    if len(file) < 3:
        name = data[2:]
    else:
        name = data[3:]
    info_list.append(file + name)


# for column in info_list:
#     new_list = []
#     first_name = column[0]
#     last_name = column[1]
#     for new_column in info_list:
#         new_first_name = new_column[0]
#         new_last_name = new_column[1]
#         if first_name == new_first_name and last_name == new_last_name:
#             if column[2] == '':
#                 column[2] = new_column[2]
#             if column[3] == '':
#                 column[3] = new_column[3]
#             if column[4] == '':
#                 column[4] = new_column[4]
#             if column[5] == '':
#                 column[5] = new_column[5]
#             if column[6] == '':
#                 column[6] = new_column[6]
#     for i in info_list:
#         if i not in new_list:
#             new_list.append(i)


new_list = []
contact_dict = {}
for column in info_list[1:]:
    last_name = ', '.join(column[:2])
    if last_name not in contact_dict:
        contact_dict[last_name] = column
    else:
        for val, item in enumerate(contact_dict[last_name]):
            if item == '':
                contact_dict[last_name][val] = column[val]


for last_name, contact in contact_dict.items():
        for contacts in contact:
            if contact not in new_list:
                new_list.append(contact)


with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)