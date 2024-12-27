#1stprogram:
"""import re
def validate_phone_number(phone_number):
    pattern = re.compile(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$')
    """r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$'"""
    if pattern.match(phone_number):
        return True
    else:
        return False

phone_number = input("Enter your phone number: ")

if validate_phone_number(phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")      """
#2nd program:
import re

class*  Student:
    def __init__(self, name, mark):
        if not name:  
            raise ValueError("Name cannot be empty<<enter your name >>")
        if not isinstance(name, str) or not re.match(r"^[a-zA-Z ]+$", name):
            raise ValueError("Name can only contain letters and spaces. Please try again.")
        if not isinstance(mark, (int, float)) or not 0 <= mark <= 100:
            raise ValueError("Mark must be a number between 0 and 100.")
        self.name = name
        self.mark = mark

    def calculate_grade(self):
        if self.mark >= 100:
            return "A"
        elif self.mark >= 89:
            return "B"
        elif self.mark >= 79:
            return "C"
        elif self.mark >= 69:
            return "D"
        else:
            return "Fail"

try:
    name = input("Enter the student's name: ")
    mark = float(input("Enter the student's mark (0-100): "))
    student = Student(name, mark)
    print(f"Name: {student.name}\nMark: {student.mark}\nGrade: {student.calculate_grade()}")
except ValueError as e:
    print(f"Error: {e}")
