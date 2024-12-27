n=int(input())
arr=[]
for i in range (n):
    L=list(map(int,input().split()))
    arr.append(L)
print(arr)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()         
