jessie_route = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
ollie_route = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 24, 26] #display the routes of the packages 

for package in ollie_route[:]:  
    if package in jessie_route:
        ollie_route.remove(package) #if the package is within jessies route remove it from oliies

print("Packages for Ollie's route:", ollie_route) #print ollies new route