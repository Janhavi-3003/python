#question01
num = int(input())
arr = [list(map(int, input().split())) for _ in range(num)]
print("Average grades for each student:")
for i, grades in enumerate(arr, start=1):
    avg = sum(grades) / len(grades)
    print(f"Student {i}: {avg:.2f}")
print("Highest grade in each subject:")
subjects = ["Maths", "Science", "English"]
high = [max(subject) for subject in zip(*arr)]
for subject, grade in zip(subjects, high):
    print(f"{subject}: {grade}")
overall_avg = sum(sum(grades) for grades in arr) / (num * len(arr[0]))
print(f"Overall class average: {overall_avg:.2f}")
#question02
num = int(input())
arr = [list(map(int, input().split())) for _ in range(num)]
print("Total quantities of each product:")
for i, quantities in enumerate(arr, start=1):
    total = sum(quantities)
    print(f"Product {i}: {total}")
product = int(input())
max_quantity = max(arr[product-1])
section = chr(65 + arr[product-1].index(max_quantity))
print(f"Section with the highest quantity for Product {product}: 
Section {val}") 
high=min(arr2) 
c=arr2.index(high) 
print(f"Product with the lowest total quantity: Product {c+1}")
