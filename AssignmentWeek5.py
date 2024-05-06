# Step 1: Create a single list containing employee information
data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# Step 2: Sort the information into a list of dictionary items
employeeInfo = []
for i in range(0, len(data), 3):
    # Ensure there is enough data for an employee record
    if (i + 2 < len(data)):
        employeeNumber = data[i]
        name = data[i + 1]
        hourlyWage = data[i + 2]

        # Check if employeeNumber and hourlyWage are numeric
        if (isinstance(employeeNumber, (int, float)) and isinstance(hourlyWage, (int, float))):
            employeeDict = {
                "employeeNumber": employeeNumber,
                "name": name,
                "hourlyWage": hourlyWage
            }
            employeeInfo.append(employeeDict)

# Step 3: Remove duplicate data
uniqueEmployeeInfo = []
for employee in employeeInfo:
    if (employee not in uniqueEmployeeInfo):
        uniqueEmployeeInfo.append(employee)

# Step 4: Add totalHourlyRate key to each dictionary item
for employee in uniqueEmployeeInfo:
    employee["totalHourlyRate"] = employee["hourlyWage"] * 1.3

# Step 5: Identify underpaid salaries
underpaid_salaries = []
for employee in uniqueEmployeeInfo:
    if (28.15 <= employee["totalHourlyRate"] <= 30.65):
        underpaid_salaries.append(employee)

# Step 6: Calculate raise for each employee and store in companyRaises
companyRaises = []
for employee in uniqueEmployeeInfo:
    hourlyRate = employee["hourlyWage"]
    if (22 <= hourlyRate < 24):
        raiseAmount = hourlyRate * 0.05
    elif (24 <= hourlyRate < 26):
        raiseAmount = hourlyRate * 0.04
    elif (26 <= hourlyRate < 28):
        raiseAmount = hourlyRate * 0.03
    else:
        raiseAmount = hourlyRate * 0.02

    companyRaises.append({"name": employee["name"], "raiseAmount": raiseAmount})

# Step 7: Print out the data
print("Employee Information:")
print(uniqueEmployeeInfo)
print("\nUnderpaid Salaries:")
print(underpaid_salaries)
print("\nCompany Raises:")
print(companyRaises)
