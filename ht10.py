#diplaying books
def display():
    if len(L) == 0:
        print("Books not available")
    else:
        print(L)
def add():
    L.append(input("Enter the book title: "))
    print(L)
def remove():
    remove_book = input("Enter the book title: ")
    if remove_book in L:
        L.remove(remove_book)
        print(L)
    else:
        print(f"{remove_book} not in Library")
n = int(input("Enter the number of books: "))
L = []
for i in range(n):
    L.append(input("Enter book title: "))
display()
add()
remove()
print("^"*30) 
#cosmetics item displays
def Display():
    print(Inventory)
def add():
    Inventory.update({"Perfumes": 500})
    print(Inventory)
def remove():
    if "Facecream" in Inventory:
        Inventory.pop("Facecream")
        print(Inventory)
    else:
        print("Facecream not in Inventory")
Inventory = {"Facecream": 250, "Foundation": 400}
Display()
add()
remove()




