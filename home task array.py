#coding 01
n1 = int(input("Enter the number of students: "))
l1= input("Enter the student names separated by space: ").split()
n2 = int(input("Enter the number of grades: "))
l2= list(map(int, input("Enter the grades separated by space: ").split()))
for i in range(n1):
    print(f"{l1[i]} {l2[i]}")
#coding 02
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)
min_element = arr[0]
for num in arr:
    if num < min_element:
        min_element = num
print(f"Minimum element = {min_element}")
#coding 03
n1 = int(input("Enter the number of elements for the first array: "))
arr1 = list(map(int, input("Enter the elements for the first array separated by space: ").split()))
n2 = int(input("Enter the number of elements for the second array: "))
arr2 = list(map(int, input("Enter the elements for the second array separated by space: ").split()))
arr1.sort(reverse=True)
arr2.sort(reverse=True)
merg_arr = arr1 + arr2
print("Merg_array in descending order: ", merged_arr)






