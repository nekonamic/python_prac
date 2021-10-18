bonus = 0
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    if sales >= 1000:
        bonus = sales * 0.15
    print("bonus: {:.0f}".format(bonus))
    sales = float(input("Enter sales: $"))
