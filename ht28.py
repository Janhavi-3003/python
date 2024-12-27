#QUESTION 1: 
class Person: 
    def __init__(self,name): 
        self.name=name 
    def display_name(self): 
        print(f"Name of the person is {self.name}") 
class Student(Person): 
    def __init__(self,name,student_id): 
        super().__init__(name) 
        self.student_id=student_id 
    def display_student_id(self): 
        print(f"Student id is {self.student_id}") 
c=Student("jaaanu","E24AI015") 
c.display_name() 
c.display_student_id() 
 
#QUESTION 2: 
class Employee: 
    def __init__(self,name,salary): 
        self.name=name 
        self.salary=salary 
    def display_details(self): 
        print("Employee name:",self.name) 
        print("Employee salary:",self.salary) 
class Manager(Employee): 
    def __init__(self,name,salary,department): 
        super().__init__(name,salary) 
        self.department=department 
    def show(self): 
        print("Employee department:",self.department) 
details=Manager("jaaanu",60000,"AI") 
details.display_details() 
details.show()
