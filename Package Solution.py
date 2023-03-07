weight = float(input("Enter the weight of the package in kg: "))

if weight <= 5:
    cost = 5
elif weight <= 10:
    cost = 10
else:
    cost = 15

print("The shipping cost for a package weighing", weight, "kg is $", cost, ".")
