#--First Scenario using Sequence Assignment statement--
#Assign hours spent on homework each day of the week in a sequence, add them up, and print total hours 
mon, tue, wed, thur, fri, sat, sun = 2, 3, 1, 4, 1, 0, 0
sumOfHours = mon + tue + wed + thur + fri + sat + sun
totalHoursDisplay = print("Total Hours Spent On Homework this week: ", sumOfHours)

#--Second Scenario using Augmented Assignment statement--
#Add 5 hours of unplanned worked hours to the expected hours worked and print 
hoursWorked = 40
hoursWorked += 8 #unplanned worked hours, add 8 hours to hoursWorkedVariable  
print ("\nTotal Hours Worked this Week: ", hoursWorked)

#--Third Scenario using swap Assignment statment--
#Swap values in boxes and print the before and after results 
boxAContents = "Books"
boxBContents = "Toys"
# Before swapping
print("\nBefore swapping:")
print("Box A contains:", boxAContents)
print("Box B contains:", boxBContents)
# Swapping the contents
boxAContents, boxBContents = boxBContents, boxAContents
# After swapping
print("\nAfter swapping:")
print("Box A contains:", boxAContents)
print("Box B contains:", boxBContents)

#--Fourth Scenario --
# Manage a shopping list using extended sequence statement 
# Initial shopping list
shoppingList = ["Apples", "Milk", "Bread"]

# User remembers more items to buy
additionalItems = ["Eggs", "Cheese", "Tomatoes"]

# Extend the shopping list with additional items
shoppingList.extend(additionalItems)

# Print the extended shopping list
print("Extended shopping list:")
for item in shoppingList:
    print(item)

#--Fifth Scenario --
# Using Multiple-Target Assignment statments, store a persons information 
# Simulating receiving data about a person
person_data = ("Maria Berry", 50, "maria.berry@whateveremail.com")
# Unpacking the received data into individual variables
name, age, email = person_data
# Printing the received information
print("Name:", name)
print("Age:", age)
print("Email:", email)
