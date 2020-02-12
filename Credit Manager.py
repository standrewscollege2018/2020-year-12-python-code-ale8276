# Manage student info about L1 NCEA credits
# 11/2/2020
# Scenario: Mr. van Florentein needs a way to view how many L1 credits students currently have

# This list stores student names
students = ["Bob", "Mary", "Lewis", "John", "Steven"]

# Display all students in a list
for index in range(0, len(students)):
    print(index + 1, students[index])

# Add a student
student_add = input("Enter a student name: ")
students.append(student_add)

# Display all students in a list
for index in range(0, len(students)):
    print(index + 1, students[index])
    
# Delete a student
student_number = int(input("Enter the name of the student you want to delete: "))
del students[student_number-1]

# Display all students in a list
for index in range(0, len(students)):
    print(index + 1, students[index])



