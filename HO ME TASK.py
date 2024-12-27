
"""#P01
main=input("Enter the main string value:")
sub=input("Enter the sub string value:")
try:
 position=main.index(sub)
 print("The element is founded at ",position)
except ValueError:
 print("The substring is not found")
"""
"""
#P0"2
grades=[]
try:
 avg=sum(grades)/len(grades)
 print("The average of the grades is",avg)
except ZeroDivisionError:
 print("The list is empty")
"""
#pro3
L=[10,20,30,40,50]
try:
 index=int(input("Enter the index value:"))
 element=L[index]
 print("The element is found",element)
except IndexError:
 print("the index is out of range")

