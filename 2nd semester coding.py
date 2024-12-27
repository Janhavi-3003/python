#ht 01 (26/11/2024)
class BankAccount: 
    def __init__(self,acc_holdername,acc_num,initial_balance=0): 
        self.acc_hname=acc_holdername 
        self.acc_num=acc_num 
        self.bal=initial_balance 
    def deposit(self,amount): 
        if amount>0: 
            self.bal+=amount 
            print("Successfully deposited") 
        else: 
            print("Invalid deposit amount") 
    def withdraw(self,amount): 
        if amount<self.bal: 
            self.bal-=amount 
            print("Successfully withdrawn") 
        else: 
            print("Not enough funds") 
    def check(self): 
        print(f"Your balance is {self.bal}") 
acc_holder=BankAccount("Anika",24365435,10000) 
acc_holder.deposit(5000) 
acc_holder.check() 
acc_holder.withdraw(1000) 
acc_holder.check() 
 
#QUESTION 2: 
class Cosmetics: 
    def __init__(self,p_name="Lipstick",p_brand="Lakme",p_price=618,p_category="Makeup"): 
        self.p_name=p_name 
        self.p_brand=p_brand 
        self.p_price=p_price 
        self.p_category=p_category 
    def display(self): 
        print(f"Product name is {self.p_name}") 
        print(f"Product brand is {self.p_brand}") 
        print(f"Product price is ${self.p_price}") 
        print(f"Product category is {self.p_category}") 
cosm=Cosmetics() 
cosm.display() 
