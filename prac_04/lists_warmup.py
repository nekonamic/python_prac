numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = "ten"
numbers[-1] = 1
numbers = numbers[2: -1:]
if 9 in numbers:
    print("9 is an element of numbers")
else:
    print("9 is not an element of numbers")
