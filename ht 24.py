class Ecommerce:
  def __init__(self, price, discount, tax):
    self.price = price
    self.discount = discount
    self.tax = tax

  def calculate(self):
    return self.price - (self.price * self.discount / 100) + (self.price * self.tax / 100)

try:
  price = float(input("Enter price: "))
  discount = float(input("Enter discount: "))
  tax = float(input("Enter tax: "))

  ecom = Ecommerce(price, discount, tax)
  print("Final price: ", ecom.calculate())

except ValueError:
  print("Invalid input. Please enter a valid number.")
