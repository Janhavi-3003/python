#1
num=int(input())
temp=num
rev=0
while temp!=0:
    dig=temp%10
    rev=(rev*10)+dig
    temp//=10
if rev==num:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")

#2
import math
sum_series=0
x=float(input("Enter the value of x:"))
n=int(input("Enter the number of terms:"))
for i in range(n+1):
    sum_series+=(x**i)/math.factorial(i)
print(sum_series)
    

#3
num=int(input())
temp=num
rev=1
while temp!=0:
    dig=temp%10
    rev*=dig
    temp//=10
print(rev)

#4
num=int(input())
fact=1
for i in range(1,num+1):
    fact*=i
    print(fact)

#5
num=int(input())
flag=0
if num>1:
    for i in range(2,num):
        if num%i==0:
            flag=0
            break
        else:
            flag=1
if flag==1:
    print("Prime")
else:
    print("Not Prime")

#6
OUTPUT:
5
6
7
8

#7
OUTPUT:
P y t h o n

#8
OUTPUT:
P ?$
y ?$
t ?$
h ?$
o ?$
n ?$

#9
64
121
196
289
400

#10
n=1
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#11
n1=100
n2=500
temp=[]
for i in range(n1,n2+1):
    if i%11==0 and i%2!=0:
        temp.append(i)
print(temp)
