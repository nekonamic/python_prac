import random

amount = int(input("How many quick picks? "))
for i in range(0, amount):
    count = 0
    j = 0
    li = []
    for j in range(0, 6):
        add = random.randint(1, 45)
        if add in li:
            while add in li:
                add = random.randint(1, 45)
            li.append(add)
        else:
            li.append(add)
    li.sort()
    for element in li:
        print("{:>2}".format(element), end=" ")
    print("")
