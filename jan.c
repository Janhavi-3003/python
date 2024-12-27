
a=int(input())
b=int(input())
if a<b:
    print(a)
else:
    print(b)
    
principal=float(input())
rate=float(input())
time=float(input())
compound_interest=principal*(1+rate/100)**time#assuming the interest is compounded annually (n=1)
print(int(compound_interest))

a=int(input())
b=int(input())
a,b=b,a
print(a,b)

L=["cricket","basketball","football"]
print("football" in L)

s="python program"
substring="test"
if substring is not in s:
    print("true")
else:
    print("false")

