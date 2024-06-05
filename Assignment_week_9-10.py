#Assignment 9-10 - Heidi Berry 6/5/2024 
#Writing program that will gather and store information about students and instructors
import re

class Validator:
    def isValidName(name):
        # Check if name contains only letters and spaces, must contain both upper and lower case 
        return bool(re.match(r'^[a-zA-Z\s]+$', name)) and any(char.islower() for char in name) and any(char.isupper() for char in name)

    def isValidEmail(email):
        # Check if email is alphanumeric and matches email format
        return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) and not re.search(r'[!\"\'#$%^&*()=+,<>/\?;:\[\]{}\\]', email)
        
    def isValidStudentId(studentId):
        # Check if studentId is a number and 7 or less digits long
        return studentId.isdigit() and len(studentId) <= 7

    def isValidInstructorId(instructorId):
        # Check if instructorId is a number and 5 or less digits long
        return instructorId.isdigit() and len(instructorId) <= 5

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        # Method to display information
        raise NotImplementedError("Subclass must implement abstract method")

class Student(Person):
    def __init__(self, name, email, studentId, programOfStudy):
        super().__init__(name, email)
        self.studentId = studentId
        self.programOfStudy = programOfStudy

    def displayInformation(self):
        # Display student's information
        print("Role: Student")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Student ID: {self.studentId}")
        print(f"Program of Study: {self.programOfStudy}\n")

class Instructor(Person):
    def __init__(self, name, email, instructorId, lastInstitution, highestDegree):
        super().__init__(name, email)
        self.instructorId = instructorId
        self.lastInstitution = lastInstitution
        self.highestDegree = highestDegree

    def displayInformation(self):
        # Display instructor's information
        print("Role: Instructor")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Instructor ID: {self.instructorId}")
        print(f"Last Institution: {self.lastInstitution}")
        print(f"Highest Degree: {self.highestDegree}\n")

def gatherStudentInformation():
    # Gather and validate student information
    print("\nEnter student information:")
    name = input("Name (letters and spaces only): ")
    while not Validator.isValidName(name):
        print("Invalid name. Please use only letters and spaces.  Name must contain upper and lower case letters.")
        name = input("Name (letters and spaces only): ")

    email = input("Email (alphanumeric characters only): ")
    while not Validator.isValidEmail(email):
        print("Invalid email. Please use only alphanumeric characters.")
        email = input("Email (alphanumeric characters only): ")

    studentId = input("Student ID (7 or less digits): ")
    while not Validator.isValidStudentId(studentId):
        print("Invalid student ID. Please enter a number that is 7 or less digits long.")
        studentId = input("Student ID (7 or less digits): ")

    programOfStudy = input("Program of Study: ")

    return Student(name, email, studentId, programOfStudy)

def gatherInstructorInformation():
    # Gather and validate instructor information
    print("\nEnter instructor information:")
    name = input("Name (letters and spaces only): ")
    while not Validator.isValidName(name):
        print("Invalid name. Please use only letters and spaces.")
        name = input("Name (letters and spaces only): ")

    email = input("Email (alphanumeric characters only): ")
    while not Validator.isValidEmail(email):
        print("Invalid email. Please use only alphanumeric characters.")
        email = input("Email (alphanumeric characters only): ")

    instructorId = input("Instructor ID (5 or less digits): ")
    while not Validator.isValidInstructorId(instructorId):
        print("Invalid instructor ID. Please enter a number that is 5 or less digits long.")
        instructorId = input("Instructor ID (5 or less digits): ")

    lastInstitution = input("Last Institution: ")
    highestDegree = input("Highest Degree: ")

    return Instructor(name, email, instructorId, lastInstitution, highestDegree)

def main():

    # Print instructional information for the user
    print("Welcome to the College Records Program!")
    print("This program will gather and store information about students and instructors.")
    print("You will be asked to input details such as name, email, student ID, instructor ID, etc.")
    print("Please ensure that the information entered is valid and follows the specified formats.")
    print("You can input multiple individuals, and once you are done, type 'done' to finish.")
    print("The program will then display all the collected information.\n")

    # List to store the records of students and instructors
    collegeRecords = []

    while True:
        # Prompt user to enter the type of individual or to finish
        individualType = input("\nEnter the type of individual (student/instructor), or 'done' to finish: ").lower()

        if individualType == 'student':
            student = gatherStudentInformation()
            collegeRecords.append(student)
        elif individualType == 'instructor':
            instructor = gatherInstructorInformation()
            collegeRecords.append(instructor)
        elif individualType == 'done':
            break
        else:
            print("Invalid input. Please enter 'student', 'instructor', or 'done'.")

    # Display all the collected records
    print("\nCollege Records:")
    for person in collegeRecords:
        person.displayInformation()
        
main()
