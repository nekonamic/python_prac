x = int(input("Enter start number: "))
y = int(input("Enter end number: "))
print("even numbers from {} to {}: ".format(x, y), end="")
for i in range(x, y, 2):
    if x % 2:
        i += 1
    print(i, end=" ")
print("\nodd numbers from {} to {}: ".format(x, y), end="")
for i in range(x, y, 2):
    if not x % 2:
        i += 1
    print(i, end=" ")
print("\nsquares from {} to {}: ".format(x, y), end="")
for i in range(x, y, 1):
    print(i ** i, end=" ")
