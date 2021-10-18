print("Electricity bill estimator")
price = float(input("Enter cents per kWh: "))
use = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))
bill = (price * use * days) / 100
print("Estimated bill: ${:.2f}".format(bill))
