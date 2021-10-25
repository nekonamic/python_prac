name = input("Enter your name: ")
with open("name.txt", "a") as out_file:
    print(name, file=out_file)

with open("name.txt", "r") as in_file:
    for line in in_file:
        print(line, end="")

with open("numbers.txt", "r") as numbers_file:
    for index, number in enumerate(numbers_file):
        if index == 0:
            number1 = number
        elif index == 1:
            number2 = number
    print(int(number1) + int(number2))

with open("numbers.txt", "r") as numbers_file:
    for number in numbers_file:
        print(number, end="")
