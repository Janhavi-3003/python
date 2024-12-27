class student:
    def __init__(self,stu_id, name, grade):
        self.stu_id=stu_id
        self.name = name
        self.grade = grade

    def validate(self):
        if not ((stu_id).startswith("STU") and (stu_id)[3:].isdigit()):
            return "Invalid ID"
        if not (len(self.name) >= 2 and self.namereplace(" ", "").isalpha()):
            return "Invalid name"
        valid_grades = [f"{i}th Grade" for i in range(1, 13)]
        if self.grade not in valid_grades:
            return "Invalid grade"
        return "Valid"

stu_id = input("Enter ID: ")
name = input("Enter Name: ")
grade = input("Enter Grade: ")

student= student(id, name, grade)
print(student.validate())
