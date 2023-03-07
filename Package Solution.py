weight = float(input("Enter the weight of the package in kg: ")) #ask for the weight

#script to determine the weight
if weight <= 5:
    cost = 5
elif weight <= 10:
    cost = 10
else:
    cost = 15

#Print the outcome
print("The shipping cost for a package weighing", weight, "kg is $", cost, ".")
