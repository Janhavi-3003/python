#1
num=int(input())
reverse=0
while num>0:
    digits=num%10
    reverse=(reverse*10)+digits
    num=num//10
print(reverse)

#2
num=int(input())
temp=num#temporary variable to check digit count
digi_count=0
while temp>0:
    temp//=10
    digi_count+=1
if digi_count==3:
    last=(num%10)**3
    middle=int((num%100)/10)**3
    first=int(num/100)**3
    add=last+middle+first
    print(add)
    if add==num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
else:
    print("Please enter 3 digit number")
