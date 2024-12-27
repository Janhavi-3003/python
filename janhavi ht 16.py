#question 1
class user():
    def __init__(self):
        self.__username = input("Enter your username: ")
        self.__password = input("Enter your password: ")

    def validate_password(self):
        if len(self.__password) < 8:
            return "Password should be at least 8 characters long"
        if not any(i.isdigit() for i in self.__password):
            return "Password should have at least one number"
        if not any(i in "!@#$%^&*_- " for i in self.__password):
            return "Password should have at least one special character"
        return "Valid"

    def check_password(self):
        result = self.validate_password()
        if result == "Valid":
            return "Password verified!!"
        else:
            return f"Password verification failed: {result}"

u = user() 
print(u.validate_password())
print(u.check_password())
print("*"*78) 

#question2
class Item:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantitytyrre

    def set_price(self, price):
        if price > 0:
            self.__price = price
            return "Price is valid"
        else:
            return "Price should not be less than 0"

    def set_quantity(self, quantity):
        if isinstance(quantity, int) and quantity > 0:
            self.__quantity = quantity
            return "Quantity is valid"
        else:
            return "Quantity should be a positive integer"

    def get_quantity(self):
        return self.__quantity

item_name = "samsung s23"
item_price = 32000
item_quantity = 9000

item = Item(item_name, item_price, item_quantity)
print(item.set_price(item_price))
print(item.set_quantity(item_quantity))
print("Quantity is", item.get_quantity())
print("*"*78)

#question3
class Learner:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def set_age(self, age):
        if 5 <= age <= 100:
            self.__age = age
            return age
        else:
            return "Invalid age"

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            return score
        else:
            return "Invalid score"

    def get_details(self):
        return f"Name: {self.__name}, Age: {self.__age}, Score: {self.__score}"

learner_name = "jaanu"
learner_age = 17
learner_score = 77

learner = Learner(learner_name, learner_age, learner_score)
print(learner.get_details())
print("*"*78)

print("<<<<<<<<<<<<<<<<the hometask completed by jaaanu>>>>>>>>>>>>>>>>>")



