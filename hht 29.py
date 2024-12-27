QUESTON 1: 
class Library: 
    def __init__(self,b_name,b_author,b_year): 
        self.b_name=b_name 
        self.b_author=b_author 
        self.b_year=b_year 
    def displayBookDetails(self): 
        print(f"Book Name:{self.b_name}\nAuthor of the 
Book:{self.b_author}\nYear of publishing:{self.b_year}") 
class Member: 
    def __init__(self,m_name,m_id,due_date): 
        self.m_name=m_name 
        self.m_id=m_id 
        self.due_date=due_date 
    def displayMemberDetails(self): 
        print(f"Member Name:{self.m_name}\nMember 
ID:{self.m_id}\nDue Date:{self.due_date}") 
class LibraryManagement(Library,Member): 
    def 
__init__(self,b_name,b_author,b_year,m_name,m_id,due_date): 
        Library.__init__(self,b_name,b_author,b_year) 
        Member.__init__(self,m_name,m_id,due_date) 
    def displayLibraryManagementInfo(self): 
        self.displayBookDetails() 
        self.displayMemberDetails() 
Lm=LibraryManagement("Harry 
Potter","J.K.Rowling",1997,"jaaanu",2303,"14-12-2024") 
Lm.displayLibraryManagementInfo() 
 
QUESTION 2: 
class Restaurant: 
    def __init__(self,restaurant_name,menu): 
        self.restaurant_name=restaurant_name 
        self.menu=menu 
    def displayMenu(self): 
        print(self.restaurant_name) 
        print(self.menu) 
class Delivery: 
    def __init__(self,rider_name,rider_contact,delivery_place): 
        self.rider_name=rider_name 
        self.rider_contact=rider_contact 
        self.delivery_place=delivery_place 
    def displayDeliveryDetails(self): 
        print(f"Rider name:{self.rider_name}\nRider 
Contact:{self.rider_contact}\nDelivery 
place:{self.delivery_place}") 
class Order(Restaurant,Delivery): 
    def 
__init__(self,restaurant_name,menu,rider_name,rider_contact,deli
 very_place): 
        Restaurant.__init__(self,restaurant_name,menu) 
        
Delivery.__init__(self,rider_name,rider_contact,delivery_place) 
    def displayOrderDetails(self): 
        self.displayMenu() 
        self.displayDeliveryDetails() 
rm=Order("buhari","\nBiriyani\nFried 
rice\nParotta\nButter 
Naan","Ram",9445020760,"pammal") 
rm.displayOrderDetails()
