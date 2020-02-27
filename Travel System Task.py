# Travel System Task
# Write a program for a travel company, that allows customers to calculate the total cost of their holiday. 

# List of overseas destinations - first index is the name of the country
#                               - second index is the price of the flight
#                               - third index is the price of the acccomadation
overseas_destination = [["Sydney", "326", "120"], ["Tonga", "378", "40"], ["Shanghai", "1436", "60"], ["London", "2376", "80"]]

# List of departure locations
departure_location = [["Auckland", "0"], ["Wellington", "50"], ["Christchurch", "75"]]

TOTAL_PRICE = 0

# Function that will be used to check whether the user has inputted an integer or a string
# The text variable is a generic term and will be replaced by text- which will be used as instructions for the user
# The max_range variable is used to keep the user from inputting an integer out of the range
# This range value changes depending on what the range is for which particular question asked
def number_check(text, max_range):

    print(text)
    user_choice = input()

    # This loop will keep going until the user inputs an integer within range

    while True:
        try:
            user_choice = int(user_choice)
            if user_choice in range(1,max_range):
                break

            else:
                print("Enter a number in range.")
                user_choice = input()

        # If the user inputs a string, it will give the user an error message as well as allow them to add another input

        except:
            print("Error! You did not enter an appropriate number. Please enter a number within the range.")
            user_choice = input()

    return user_choice

# Funtion that prints out the list of the destinations
# Location_list variable as a generic value that can be replaced by any chosen list
def location_list_details(location_list):
    
    # Prints out list of locations of any chosen list 
    for i in range(0, len(location_list)):
        print(i+1, location_list[i][0])

# Print out the price details for the locations chosen
def price_details(value):
    
    # Make total price global so that the value can be used in other functions
    global TOTAL_PRICE
    
    # Calculates GST of the prices
    gst = (TOTAL_PRICE + value) * 0.15
    
    # Total price including GST
    TOTAL_PRICE = TOTAL_PRICE + value + gst
    
    # Prints out total price to 2 decimal places
    print(f"\nYour total current price is ${TOTAL_PRICE:.2f} including GST.\n")

# Function that asks the user to confirm whether or not they chose the right destination
def book_flight_confirmation(location_list, text):

    # Make user option global so that the value can be used in other functions
    global user_option
    
    # Start while loop to keep going until user breaks the loop
    ask = True
    while ask == True: 
        
        # Prints list of locations
        location_list_details(location_list)
        
        # Input that asks user to choose an option
        user_option = number_check("\nPlease enter the number of {}: ".format(text),len(location_list)+1)
        
        # Input that asks user to confirm an option
        user_confirm = number_check("Is {} {}?\n1) Yes\n2) No\nPlease choose a number: ".format((location_list[user_option - 1][0]), text), len(location_list)+1)
        
        # If user chooses option 1, stop the while loop and continue with the program
        if user_confirm == 1:
            print("Cool! Let's continue.")
            ask = False
        
        # If user chooses option 2, continue with this while loop
        elif user_confirm == 2:
            continue
  
# function to book user's flight
def book_flight():
    
    # Takes the user_option value from previous function
    global user_option
    
    # Starts up function to confirm departure location
    book_flight_confirmation(departure_location, "your departure location")

    # If user chooses option 1, start price_details function and add $0 
    if user_option == 1:
        price_details(int(departure_location[user_option - 1][1]))

    # If user chooses option 1, start price_details function and add $50   
    elif user_option == 2:
        price_details(int(departure_location[user_option - 1][1]))

    # If user chooses option 1, start price_details function and add $75
    elif user_option == 3:
        price_details(int(departure_location[user_option - 1][1]))      
  
    # Starts up function to confirm overseas destination
    book_flight_confirmation(overseas_destination, "your overseas destination")
    
    # If user chooses option 1, start price_details function with a $326 value
    if user_option == 1:
        price_details(int(overseas_destination[user_option - 1][1]))      
    
    # If user chooses option 2, start price_details function with a $378 value
    elif user_option == 2:
        price_details(int(overseas_destination[user_option - 1][1]))  

    # If user chooses option 3, start price_details function with a $1436 value
    elif user_option == 3:
        price_details(int(overseas_destination[user_option - 1][1]))  
        
    # If user chooses option 4, start price_details function with a $2376 value
    elif user_option == 4:
        price_details(int(overseas_destination[user_option - 1][1]))  
        
    # Asks user for the number of nights they are staying
    user_accomodation = number_check("Enter the number of nights you are staying: ", 100)
    
    # If less than 3 nights, start up price_details function and charge accomodation price per night
    if user_accomodation < 3:
        price_details(int(overseas_destination[user_option - 1][2]) * user_accomodation)
       
    # If less than 3 nights, start up price_details function and charge only 80% of accomodation price    
    if user_accomodation == 3 or user_accomodation > 3:
        price_details(int(overseas_destination[user_option - 1][2]) * user_accomodation * 0.80)
    
    print("Perfect! You have just booked your flight! The total price for your flight and accomodation adds up to: ${}".format(TOTAL_PRICE))
    
# Menu function that sends the user to different options depending on what they choose
def menu_choice():

    # If user chooses option 1, start the location_list_details function with departure_location list
    if user_choice == 1:
        location_list_details(departure_location)

    # If user chooses option 2, start the location_list_details function with overseas_destination list
    elif user_choice == 2:
        location_list_details(overseas_destination)
        
    # If user chooses option 2, start the book_flight function           
    elif user_choice == 3:
        book_flight()
        
    # If user chooses option 4, end the program
    elif user_choice == 4:
        ask = False

# Allow user to choose an option
print("What would you like to do?\n\n1) View departure locations\n2) View overseas destinations\n3) Book flight\n4) Exit\n")
user_choice = number_check("Please enter the number of the option you wish to do: ", 5)

# Start menu_choice function
menu_choice()

# Runs function on a while loop until the user chooses option 4 to exit the program
while user_choice != 4:
    
    # Allow user to choose an option
    print("What would you like to do?\n\n1) View departure locations\n2) View overseas destinations\n3) Book flight\n4) Exit\n")
    user_choice = number_check("Please enter the number of the option you wish to do: ", 5)
    
    # Start menu_choice function
    menu_choice()