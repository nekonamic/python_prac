name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print("My guitar: {}, first made in {}".format(name, year))

print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

print("My {} was first made in {} (that's right, {}!)".format(name, year, year))

print("My {} would cost ${:,.2f}".format(name, cost))
print("My {} would cost ${:,.2f}".format(name, cost))

numbers = [1, 19, 123, 456, -25]
for number in numbers:
    print("Number is {:>5}".format(number))

for i, number in enumerate(numbers, 1):
    print("Number {} is {:>5}".format(i, number))
