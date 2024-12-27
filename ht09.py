
# Check whether a number is prime or not:
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("yes")
else:
    print("no")
# Find the factorial of a number:
n = int(input( ))
result = 1
for i in range(1, n + 1):
    result *= i
print("Factorial:", result)
#. Find the Fibonacci series up to N number:
n = int(input())
a, b = 0, 1
result = []
for i in range(n):
    result.append(a)
    a, b = b, a + b
print("Fibonacci series:", result)
# Check whether a number is divisible by 11 or not:
n = int(input("Enter a number: "))
digits = [int(x) for x in str(n)]
odd_sum = sum(digits[::2])
even_sum = sum(digits[1::2])
if (odd_sum - even_sum) % 11 == 0:
    print("Divisible by 11")
else:
    print("Not divisible by 11")
# Find the factors of a number:
n = int(input("Enter a number: "))
result = []
for i in range(1, n + 1):
    if n % i == 0:
        result.append(i)
print("Factors:", result)
