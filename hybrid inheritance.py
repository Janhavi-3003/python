class person:
    def __init__(self ,name ,age ):
        self.name=name
        self.age=age
    def person_info(self):
        print(f"Name of the student:{self.name}\nAge of the student:{self.age}")
class student(person):
    def __init__(self,stu_id):
        self.stu_id=stu_id
    def stu_info(self):
        print(f"student ID :{self.stu_id}")
class employee(person):
    def __init__(self,emp_id):
            self.emp_id=emp_id
    def employee_info(self):
        print(f"employee ID :{self.emp_id}")
class details(student,employee,person):
    def __init__(self ,name ,age,stu_id,emp_id):
        person.__init__(self ,name ,age)
        student.__init__(self,stu_id)
        employee.__init__(self,emp_id)
    def display(self):
        self.person_info()
        self.stu_info()
        self.employee_info()
j=details("JANHAVI N.K",17,"E24AI015","PREP20030")
j.display()

        
        
                
