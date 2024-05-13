#Assignment #5
import re

# Functions for data validation
def validateEmployeeId(employeeId):
    return employeeId.isdigit() and len(employeeId) <= 7

def validateEmployeeName(employeeName):
    return any(char.islower() for char in employeeName) and any(char.isupper() for char in employeeName)

def validateEmail(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) and not re.search(r'[!\"\'#$%^&*()=+,<>/\?;:\[\]{}\\]', email)

def validateAddress(address):
    return address is None or (re.match(r'^[a-zA-Z0-9\s]+$', address) and not re.search(r'[!\"\'@$%^&*_+=<>?;:[\]{}()]', address))

def validateSalary(salary):
    try:
        salary = float(salary)
        return 18 <= salary <= 27
    except ValueError:
        return False

# Function to get employee information
def getEmployeeInfo():
    employeeId = input("Enter employee ID (7 or less digits): ")
    while not validateEmployeeId(employeeId):
        employeeId = input("Invalid input. Enter employee ID (7 or less digits): ")

    employeeName = input("Enter employee name: ")
    while not validateEmployeeName(employeeName):
        employeeName = input("Invalid input. Enter employee name: ")

    employeeEmail = input("Enter employee email address: ")
    while not validateEmail(employeeEmail):
        employeeEmail = input("Invalid input. Enter employee email address: ")

    employeeAddress = input("Enter employee address (optional, press Enter to skip): ").strip()
    if employeeAddress and not validateAddress(employeeAddress):
        employeeAddress = input("Invalid input. Enter employee address (optional, press Enter to skip): ").strip()

    # Prompt the user until a valid salary is entered
    while True:
        employeeSalary = input("Enter employee salary (between 18 and 27): ")
        if validateSalary(employeeSalary):
            employeeSalary = float(employeeSalary)
            break
        else:
            print("Invalid input. Salary must be a number between 18 and 27.")
    return {
        "Employee ID": int(employeeId),
        "Employee Name": employeeName,
        "Employee Email": employeeEmail,
        "Employee Address": employeeAddress,
        "Employee Salary": employeeSalary
    }

#Intro to program 
print("Welcome to the Employee Information Program!")
print("Please provide the following details for each employee:")
print("\n1. Employee ID: This is a number that is 7 or less digits long.")
print("2. Employee Name: This should be comprised primarily of upper and lower case letters.")
print("   Spaces, the ' and - characters are allowed.")
print("3. Employee Email Address: This should be primarily alphanumeric and cannot contain: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\ ")
print("4. Employee Address (optional): If provided, it should be primarily alphanumeric and cannot contain: ! \" ' @ $ % ^ & * _ = + < > ? ; : [ ] { }")
print("5. Employee Salary: This must be a number between 18 and 27.")
print("\nPlease make sure to provide accurate information for each field.")
print("\n----------------------------------------------------------------") 

# Get employee information from user
employeeList = []
while True:
    employeeInfo = getEmployeeInfo()
    employeeList.append(employeeInfo)
    add_more = input("Do you want to enter more employee information? (yes/no): ").lower()
    if add_more != "yes":
        break

# Apply modifications using list comprehensions
employeeList = [
    {
        # Employee ID remains the same
        "Employee ID": employee["Employee ID"],
        # Append " - IT Department" to each employee's name
        "Employee Name": employee["Employee Name"] + " - IT Department",
        # Employee Email remains the same
        "Employee Email": employee["Employee Email"],
        # Employee Address remains the same
        "Employee Address": employee["Employee Address"],
        # Increase salary by 30%
        "Employee Salary": employee["Employee Salary"] * 1.3
    }
    for employee in employeeList
]

# Print the updated employee list
print("\nList of Employee Information:")
for employee in employeeList:
    print(employee)