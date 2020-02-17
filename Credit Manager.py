# Manage student info about L1 NCEA credits
# 11/2/2020
# Scenario: Mr. van Florentein needs a way to view how many L1 credits students currently have

# Display all students in a list
def display_all_students():
    for index in range(0, len(students)):
        print(index + 1, students[index])    

# This list stores student names
students = ["Bob", "Mary", "Lewis", "John", "Steven"]
    
# Display all students in a list
display_all_students()
    
# Add a student
student_add = input("Enter a student name: ")
students.append(student_add)
    
# Display all students in a list
display_all_students()
        
# Delete a student
student_number = int(input("Enter the number of the student you want to delete: "))
del students[student_number-1]
    
# Display all students in a list
display_all_students()
    
# Change student details
# Get details of which student to change and what the updated name is
student_number = int(input("Enter number of student to change: "))
new_name = input("Enter updated name: ")
new_total = input("Enter updated total: ")
    
# Change student details
students[student_number - 1] = new_name

students[student_number - 1][0] = new_total
    
# Display all students in a list
display_all_students()
