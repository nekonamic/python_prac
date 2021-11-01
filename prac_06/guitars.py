from prac_06.guitar import Guitar
print("My guitars!")
guitar_list = [[]]
count = 0
while True:
    guitar_list.append([])
    guitar_list[count].append(input("Name: "))
    if guitar_list[count][0] == "":
        break
    guitar_list[count].append(int(input("Year: ")))
    guitar_list[count].append(int(input("Cost: ")))
    print("{} ({}) : ${} added.\n".format(guitar_list[count][0], guitar_list[count][1], guitar_list[count][2]))
    guitar_list[count] = Guitar(guitar_list[count][0], guitar_list[count][1], guitar_list[count][2])
    count += 1
print("These are my guitars:")
for index in range(0, count):
    print(f"Guitar {index + 1}: {guitar_list[index].__str__()}")
