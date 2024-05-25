#Assignment #6 - v2 of assignment #5 
import re
import json

# Function to validate employee ID, checks if number that is 7 or less digits long.
def validateEmployeeId(employeeId):
    return employeeId.isdigit() and len(employeeId) <= 7

# Function to validate employee name, checks if value contains both upper and lower case letters
def validateEmployeeName(employeeName):
    return any(char.islower() for char in employeeName) and any(char.isupper() for char in employeeName)

# Function to validate email, checks if valid email format.
def validateEmail(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

# Function to validate address, checks if only alphanumeric characters and spaces
def validateAddress(address):
    return address == "" or re.match(r'^[a-zA-Z0-9\s]+$', address)

# Function to validate salary, checks if value is a number between 18 and 27
def validateSalary(salary):
    try:
        salary = float(salary)
        return 18 <= salary <= 27
    except ValueError:
        return False

# Function to get validated input from the user
def getValidatedInput(prompt, validationFunction):
    userInput = input(prompt)
    while not validationFunction(userInput):
        userInput = input(f"Invalid input. {prompt}")
    return userInput

# Function to get employee information
def getEmployeeInfo():
    employeeId = getValidatedInput("Enter employee ID (7 or less digits): ", validateEmployeeId)
    employeeName = getValidatedInput("Enter employee name: ", validateEmployeeName)
    employeeEmail = getValidatedInput("Enter employee email address: ", validateEmail)
    
    employeeAddress = input("Enter employee address (optional, press Enter to skip): ").strip()
    while employeeAddress and not validateAddress(employeeAddress):
        employeeAddress = input("Invalid input. Enter employee address (optional, press Enter to skip): ").strip()

    employeeSalary = getValidatedInput("Enter employee salary (between 18 and 27): ", validateSalary)
    employeeSalary = float(employeeSalary)

    return {
        "Employee ID": int(employeeId),
        "Employee Name": employeeName,
        "Employee Email": employeeEmail,
        "Employee Address": employeeAddress,
        "Employee Salary": employeeSalary
    }

# Function to modify employee information with list comprehension 
def modifyEmployeeInfo(employeeList):
    return [
        {
            "Employee ID": employee["Employee ID"],
            "Employee Name": getEmployeeNameValue(employee["Employee Name"]),
            "Employee Email": employee["Employee Email"],
            "Employee Address": employee["Employee Address"],
            "Employee Salary": getSalaryValue(employee["Employee Salary"])
        }
        for employee in employeeList
    ]

# Function calculates the new salary by increasing the original salary by 30% and rounding it to two decimal places.
def getSalaryValue(salary):
    return round(salary * 1.3, 2) 

# Function appends " - IT Department" to the employee name.  
def getEmployeeNameValue(empName):  
    return empName + " - IT Department"

# Function to write employee data to a JSON file
def writeToJsonFile(employeeList, filename="employeeData.json"):
    with open(filename, 'w') as file:
        json.dump(employeeList, file, indent=4)

# Function to display intro to program
def displayIntroMessage():
    print("Welcome to the Employee Information Program!")
    print("Please provide the following details for each employee:")
    print("\n1. Employee ID: This is a number that is 7 or less digits long.")
    print("2. Employee Name: This should contain both upper and lower case letters.")
    print("3. Employee Email Address: This should be a valid email format.")
    print("4. Employee Address (optional): If provided, it should contain only alphanumeric characters and spaces.")
    print("5. Employee Salary: This must be a number between 18 and 27.")
    print("\nPlease make sure to provide accurate information for each field.")
    print("\n----------------------------------------------------------------")

#main function - runs main program 
def main():
    displayIntroMessage()
    # Get employee information from user
    employeeList = []
    while True:
        employeeInfo = getEmployeeInfo()
        employeeList.append(employeeInfo)
        addMore = input("Do you want to enter more employee information? (yes/no): ").lower()
        if addMore != "yes":
            break

    # Modify employee information
    employeeList = modifyEmployeeInfo(employeeList)

    # Write the updated employee list to a JSON file
    writeToJsonFile(employeeList)

    # Print the updated employee list
    print("\nList of Employee Information:")
    for employee in employeeList:
        print(employee)
        
main()