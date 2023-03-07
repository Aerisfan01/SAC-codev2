# ask the user for a list of package weights
package_weights = input("Enter package weights separated by spaces: ")
package_weights = list(map(float, package_weights.split()))

# calculate the average of the package weights
average_weight = sum(package_weights) / len(package_weights)

# determine the discounted cost based on the average weight
if average_weight <= 5:
    discounted_cost = 4.50 * 8
elif average_weight <= 10:
    discounted_cost = 9 * 8
else:
    discounted_cost = 14 * 8

# display the discounted cost to the user
print("Discounted cost to ship 8 packages: $%.2f" % discounted_cost)
