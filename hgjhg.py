n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print("The Sorted array is:", end=" ")
for num in arr:
    print(num, end=" ")
