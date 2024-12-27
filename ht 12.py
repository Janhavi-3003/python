#1
def stu_details(name,age,department):
    print(f"Student name:{name}")
    print(f"Student Age:{age}")
    print(f"Student Department:{department}")
stu_details(name="janu",age=18,department="computer Science With Ai")
print("^"*28)
#2
def myFavfood(VDict):
    print(VDict)
foodtype=input("enter the food type:  ")
itemname=input("enter the itemname:  ")
itemcost=input("enter the itemcost:  ")
Food_items={
    'Foodtype':foodtype,
    'itemname':itemname,
    'foodcost':itemcost
    }
myFavfood(Food_items)
