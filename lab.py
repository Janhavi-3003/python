j=input()
upper=0
lower=0
for i in j:
    if i .isupper():
        upper+=1
    if i.islower():
        lower+=1
print("the upper character :",upper)
print("the lower character :",lower)

n=input()
rev=n[::-1]
print("<<<your expected output>>>")
if n==rev:
      print("palindrome")
else:
    print("not palindrome")
