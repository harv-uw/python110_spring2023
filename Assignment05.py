# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using list and files
# Change Log: (Who, When, What)
#   Zach Harvey,11.13.2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json
import os

# Define the Data Constants
MENU: str = ('---Course Registration Program---\n Select from the following menu:\n 1. Register a Student for a '
             'Course\n 2. Show current data\n 3. Save data to a file\n 4. Exit the program\n'
             '---------------------------------')
FILE_NAME: str = 'Enrollments.json'
# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file_obj = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

# Initialize data from the file if it exists or error if not
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("JSON file must exist before running this script!")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("A non-specific error occurred")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')

# Present and Process the data
# Present the menu of choices
while True:
    print(f'\n{MENU}\n')
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Please enter the student's last name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the course name: ")

            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            continue
        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("A non-specific error occurred")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
    # Present the current data
    elif menu_choice == "2":
        if not students:
            print('There is no data currently stored.')
        else:
            for student in students:
                print(f'{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        continue
    elif menu_choice == "3":
        try:
            file_obj = open(FILE_NAME, "w")
            json.dump(students, file_obj)
            file_obj.close()
            print(f'Your data was written to the file {FILE_NAME}')
            continue
        except TypeError as e:
            print("Please check that the data is in a valid JSON format")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("A non-specific error occurred")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')

    # Stop the loop
    elif menu_choice == "4":
        print('Exiting...')
        break
    # Default case
    else:
        print("\nPlease enter a menu option.")



