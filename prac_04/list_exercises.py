def first_number(li):
    return li[0]


def last_number(li):
    return li[-1]


def smallest_number(li):
    return min(li)


def largest_number(li):
    return max(li)


def average_of_the_numbers(li):
    return sum(li) / len(li)


numbers_list = []
for i in range(0, 5):
    numbers_list.append(int(input("Number: ")))
print("The first number is ", first_number(numbers_list))
print("The last number is ", last_number(numbers_list))
print("The smallest number is ", smallest_number(numbers_list))
print("The largest number is ", largest_number(numbers_list))
print("The average of the numbers is ", average_of_the_numbers(numbers_list))
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
