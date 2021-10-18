num = int(input("Number of items: "))
total = 0
for i in range(0, num, 1):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(num, total))
