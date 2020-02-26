# Travel System Task
# Write a program for a travel company, that allows customers to calculate the total cost of their holiday. 

# List of overseas destinations - first index is the name of the country
#                               - second index is the price of the flight
#                               - third index is the price of the acccomadation
overseas_destinations = [["Sydney", "326", "120"], ["Tonga", "378", "40"], ["Shanghai", "1436", "60"], ["London", "2376", "80"]]

# List of departure locations
departure_location = [["Auckland", "0"], ["Wellington", "50"], ["Christchurch", "75"]]

# Prints out list of countries
for i in range(0, len(overseas_destinations)):
    print(i+1, overseas_destinations[i][0])
    



