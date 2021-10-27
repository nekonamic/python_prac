import re


def get_name(email_in_fun):
    email_li = email_in_fun.split("@")
    name_in_fun = email_li[0]
    name_in_fun = re.sub("[^0-9a-zA-Z]+", " ", name_in_fun)
    name_in_fun = name_in_fun.title()
    return name_in_fun


emails_dict = {}
email = input("Email: ")
while email != "":
    operation = input("Is your name {}? (Y/n)".format(get_name(email)))
    if operation.lower() == "y" or operation.lower() == "yes":
        emails_dict[email] = get_name(email)
    elif operation.lower() == "n" or operation.lower() == "no":
        name = input("Name: ")
        emails_dict[email] = name
    else:
        print("Valid input")
        continue
    email = input("Email: ")
for key, value in emails_dict.items():
    print(value, key)
