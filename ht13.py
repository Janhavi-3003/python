
#question01
def create_list(*args):
    return list(args)
n = create_list(1, 2, 3)
print(n)  # [1, 2, 3]
print("|_|"*28)
#question02
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
print("|_|"*28)
#question 03
def multiply(a, b):
    return a * b
result = multiply(5, 10)
print(result)
print("|_|"*28)
#question04
def full_name(first, last):
    return first + ' ' + last
print(full_name('janu', 'krish'))
print("|_|"*28)
#question05
def square():
    n = int(input("Enter a number: "))
    print(n * n)
    print("|_|"*28)
    

square()
