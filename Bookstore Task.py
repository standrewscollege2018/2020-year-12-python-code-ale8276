# Bookstore Task
# Write a program that would be used by an administrator to maintain the catalogue for a bookstore

# List of book titles, author names and book prices
book_title = ["The Hunger Games", "To Kill a Mockingbird", "The Golden Compass"]
book_author = ["Suzanne Collins", "Harper Lee", "Philip Pullman"]
book_price = ["17.09","15.25","19.19"]

# Function that will be used to check that the user inputs a string
# This function will keep going until the user inputs a string
def blank_check(text):
    string_input = input(text)

    # While loop that will keep going until a string is inputted

    while True:
        if string_input:
            break

        # If the user does not input anything, i.e blank input, then an error message will be printed out
        # User will be prompted with an input

        else:
            print("Error! Please try again.")
            string_input = input()

    return string_input

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

# Function that allows the user to see the total number of books and details about it
def book_details():
    print("\nThere is a total of {} book(s) in stock:\n".format(len(book_title)))
    for title, author, name in zip(book_title, book_author, book_price):
        print("Title: {}, Author: {}, Price: {}".format(title, author, name))

# Function that allows the user to edit their book details
def book_edit():
    
    user_option = number_check("What would you like to change?\n1) Book title\n2) Author name\n3) Book price",4)
    
    # If user chooses option 1, the function change_details will start up along with the list of book titles 
    if user_option == 1:
        change_details(book_title, 1)

    # If user chooses option 2, the function change_details will start up along with the list of book authors  
    elif user_option == 2:
        change_details(book_author, 2)

    # If user chooses option 3, the function change_details will start up along with the list of book prices        
    elif user_option == 3:
        change_details(book_price, 3)

# Function that will display the list of book names
def title_list(book_list):

    counter = 0
    
    # For loop that will print the title of all the books in a list
    for title in book_list:
        
        # Counter used to bullet point each book
        counter = counter + 1
        
        # Print out the bullet points along with the title of the book
        print(counter, ":", title)    
    
def details_blank_check():
    
    global new_details

    # Input that allows the user to update the details of a book
    new_details = blank_check("Enter the updated details of the book: ")
        

def details_number_check():
    
    global new_details

    # Input that allows the user to update the details of a book
    new_details = number_check("Enter the updated details of the book: ",100001)
        
        
# Function used to allow users to change details about a book
def change_details(book_list, user_option):
    
    # Function that is used to print out the list of books
    title_list(book_title)
          
    # Input that allows the user to choose which book to edit  
    user_choice = number_check("Which book would you like to edit?\n", (len(book_title)+1))
    
    if user_option == 3:
        details_number_check()
    
    if user_option == 1 or user_option == 2:
        details_blank_check()
    
    # Adds the updated details to the list
    book_list[user_choice - 1] = new_details
    
    # Prints out the new details
    title_list(book_list)

# Function used to allow the user to add a book
def add_book():
 
     # Allows user to add the book they want   
    book_add = blank_check("Enter the name of a book to add: ")
    book_title.append(book_add)
    
    author_add = blank_check("Enter the name of the author: ")
    book_author.append(author_add)
    
    price_add = number_check("Enter the price of the book: ", 10001)
    book_price.append(price_add)
     
    # Print the updated list of books
    
    book_details()

# Function used to remove books
def remove_book():
    
    title_list(book_title)
     
     # Allows user to remove the book they want
    book_number = number_check("Enter the number of a book to delete: ", (len(book_title)+1))
    del book_title[book_number - 1]
     
    # Print the updated list of books    
    title_list(book_title)
     
            
# Add menu choice functionality
def menu_choice():
    
    # Add a greeting, 
    print("Welcome to Alyssa's bookstore!")
    
    ask = True
    while ask == True:
        # Add user input
        user_choice = number_check("\nWhat would you like to do?\n1) Show book details\n2) Edit book details\n3) Add book details\n4) Delete book details\n5) Close bookstore\n", 6)
        
        # If user chooses option 1, the function book_details will print out a list of books
        if user_choice == 1:
            book_details()
            
        # If user chooses option 2, the function book_edit will start up  
        elif user_choice == 2:
            book_edit()
            
        # If user chooses option 3, the function add_book will start up  
        elif user_choice == 3:
            add_book()
        
        # If user chooses option 4, the function remove_book will start up      
        elif user_choice == 4:
            remove_book()
            
        # If user chooses option 5, prints a thank you message
        elif user_choice == 5:
            print("Thank you for coming to Alyssa's bookstore!")
            ask = False
        
# Starts up the menu
menu_choice()
