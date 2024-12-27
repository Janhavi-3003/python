#QUESTION 1:

def new():
    n = int(input())
    lst = []
    for i in range(n):
        result = int(input())
        lst.append(result)
    return lst
result= new()
print(result)
#QUESTION 2:
def factorial():
    n = int(input())
    fac= 1
    for i in range(1, n + 1):
        fac*= i
    return fac 
f = factorial()
print("Factorial =", f)
#QUESTION 3:
def product(a, b):
    result = a * b
    return result
a = int(input())
b = int(input())
pro = product(a, b)
print("Product =", pro)
#QUESTION 4:
def name(first, last):
    print(first, end=" ")
    print(last, end=" ")
first = input()
last = input()
name(first, last)
# QUESTION 5:

def square(a):
    ans= a ** 2
    return ans
num = int(input())
sqr = square(num)
print("Square =", sqr)
