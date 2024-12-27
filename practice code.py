class office:
    def _init_(self,name,ID, salary):
        self.name=name
        self.ID=ID
        self.salary=salary
    def employee_details(self):
        print("employee name:",self.name)
        print("ID:",self.ID)
        print("salary:",self.salary)
class attendance:
    def _init_(self,percentage):
        self.percentage=percentage
    def display(self):
        print("your percentage:",self.percentage)
class experience(office,attendance):
    def _init_(self,name,ID,percentage,experience_tcs):
        office_init_(self,name,ID,salary)
        experience._init_(self,percentage)
        self.experience_tcs=experience_tcs
    def salaryInfo(self):
        self.employee_details()
        self.display()
        print("experince tcs:",self.experience_tcs)
name=input("Enter your name:")
ID=input("Enter your ID:")
salary=input("Enter your salary:")
percentage=input("Enter your attendance percentage")
experience=input("Enter the year experience in tcs")
jk=(name,ID,salary, percentage,experience)
jk.display()

        
