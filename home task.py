QUESTION 1:
s1={10,20,30,40,50}
s2={10,20}
subset=False
for i in s1:
 if i in s2:
 subset=True
 else:
 subset=False
if subset==True:
 print("s2 is a subset of s1")
else:
 print("s2 is not a subset of s1")
QUESTION 2:
t=(20,50,42,65,36,98)
new=t[2:6]
print(new)
QUESTION 3:
t1=tuple(map(int,input("Enter 4 elements:").split()))
a,b,c,d=t1
print(a,b,c,d,sep="\n")
QUESTION 4:
list_t=[(2, 5), (9, ), (8, 7, 6), (4, ), (12, 4, 16, 7)]
K=3
for i in range(len(list_t)):
 if len(list_t[i-1])==K:
 list_t.remove(list_t[i-1])
print(list_t)
QUESTION 5:
t_s=("Anika","M","B")
s=" "
for i in range(len(t_s)):
 s+=t_s[i]
print(s)
QUESTION 6:
l_t=[("Name","Anika"),("Age",18)]
d=dict(l_t)
print(d)
QUESTION 7:
n=int(input())
for i in range(n,0,-1):
 print(" "*(n-i)+"* "*i)
for i in range(1,n+1):
 print(" "*(n-i)+"* "*i)
