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

