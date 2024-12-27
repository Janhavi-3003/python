#program-1
num=int(input())
if num % 2 == 0:
        print("Even")
else:
        print("Odd")


#program-2
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#program-4
string=str(input())
if string.islower():
    print("lowercase")
elif string.isupper():
    print("uppercase")
else:
    print("combination of both")

#program-3
a=int(input())
b=int(input())
c=int(input())
total=a+b+c
percentage=float(total/300)*100
print(total)
print(f"{b:.2f}")
if percentage>90:
        print("eligible ")
else:
        print("not eligible")
