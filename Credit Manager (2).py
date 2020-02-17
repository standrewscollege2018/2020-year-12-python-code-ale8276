# Manage student info about L1 NCEA credits
# 11/2/2020
# Scenario: Mr. van Florentein needs a way to view how many L1 credits students currently have

# This list stores student names and credit scores
students = [["Bob", 82], ["Mary",57], ["Lewis", 101], ["John", 32], ["Steven", 67]]

# Display all students in a list
def display_all_students():
    for index in range(0, len(students)):
        print(index + 1, students[index])  
        
# Add functionality to add a student        
def add_student():
    # Add a student
    student_add = input("Enter a student name: ")
    students.append(student_add)

# Add functionality to delete a student
def delete_student():
    
    # Delete a student
    student_number = int(input("Enter the number of the student you want to delete: "))
    del students[student_number-1]
    
# Add functionaly to change student details
def change_student_details():
    
    # Change student details
    # Get details of which student to change and what the updated name is
    student_number = int(input("Enter number of student to change: "))
    new_name = input("Enter updated name: ")
    
    # Change student details
    students[student_number - 1] = new_name

# Print a greeting
print("Welcome! This programme holds all student information from StAC!\n")

# Let user choose one of the 5 options
user_input = int(input("Choose your option!\n\n1) View list of students\n2) Add a student\n3) Delete a student\n4) Change student details\n5) Stop Programme\n"))

# Added a while loop to give user the option to choose between 4 options
ask = True
while ask == True:
    
    # If user chooses 1, start function to display all students
    if user_input == 1:
        display_all_students()
        ask = False
    
    # If user chooses 2, start function to add a student
    elif user_input == 2:
        add_student()
        ask = False
    
    # If user chooses 3, start function to delete a student
    elif user_input == 3:
        display_all_students()
        delete_student()
        ask = False
    
    # If user chooses 4, start function to display and change student details
    elif user_input == 4:
        display_all_students()
        change_student_details()
        ask = False
    
    # If user chooses anything else, code breaks
    else:
        break