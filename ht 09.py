#smartphone program 

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print(f"Taking a photo with resolution: {self.resolution}MP")

class Phone:
    def __init__(self, prize):
        self.prize = prize

    def make_call(self):
        print(f"Making a call")

class Smartphone(Camera, Phone):
    def __init__(self, brand, model, resolution, prize):
        Camera.__init__(self, resolution)
        Phone.__init__(self, prize)
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"The brand new phone info details")
        print(f"Brand: {self.brand}\nModel: {self.model}\nResolution: {self.resolution}MP\nPrize: {self.prize}")

j = Smartphone("iPhone", "15 Pro", "55", "80k")
j.display_info()
j.take_photo()
print("_"*30)


#Student Athlete Program


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def student_info(self):
         print(f"the athlete student info")
         print(f"Name: {self.name}\nCourse: {self.course}")

class StudentAthlete(Student):
    def __init__(self, name, course, sport):
        super().__init__(name, course)
        self.sport = sport

    def display_athlete_info(self):
        self.student_info()
        print(f"Sport: {self.sport}")
        

s = StudentAthlete("Jaanu", "bsc cs (ai)", "uno")
s.display_athlete_info()
print("_"*30)
