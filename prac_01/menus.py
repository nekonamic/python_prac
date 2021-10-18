name = str(input("Enter name: "))
print("(H)ello\n(G)oodbye\n(Q)uit\n>>> ", end="")
option = str(input())
while True:
    if option == "H":
        print("Hello {}".format(name))
    elif option == "G":
        print("Goodbye {}".format(name))
    elif option == "Q":
        break
    else:
        print("Invalid choice")
    option = str(input(">>> "))
