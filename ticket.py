class customer:
    def __init__(self,cus_id,name, ph_no):
        self.cus_id=cus_id
        self.name=name
        self.phone=ph_no
    def generate_cust_id(self):
        co_id=random.randint(10000,99999)
        return f"TICK{co_id}"
    def veri_cus_id(cus_id):
        if cus_id[0:4]=="TICK"and cus_id[4:8].isdigit():
            print("verfication completed, your id is valid")
        else:
               print("your id invalid or create new id")

print("**Welcome to TICKET Booking applications*****")
cus_id=input("Enter the customer id:")
if Customer.verify_customer_id(cus_id):
name=input("Enter name :")
ph_no=int(input("Enter the phone number:"))
          customer=Customer(cus_id,name,ph_no)
          print("***booking details***")
          else:
              print("***invalid register***")
              name=input("enter your name :")
              ph_no=int(input("enter you phone no"))
              cus_id=customer.gen_rand_id()
              customer=Customer(cus_id,name,ph_no)
              print("your customer id:",cus_id)
              

                        print(" <<<valid!!!!!!!view the booking details>>>")
          
