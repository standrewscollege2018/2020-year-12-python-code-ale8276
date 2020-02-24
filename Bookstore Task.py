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

