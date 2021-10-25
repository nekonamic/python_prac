def celsius_to_fahrenheit(in_celsius):
    in_fahrenheit = in_celsius * 9.0 / 5 + 32
    return in_fahrenheit


def fahrenheit_to_celsius(in_fahrenheit):
    in_celsius = 5 / 9 * (in_fahrenheit - 32)
    return in_celsius


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
