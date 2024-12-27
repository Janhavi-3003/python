#QUESTION 01
r, c = map(int, input().split())
mat1 = []
mat2 = []
for _ in range(r):
    L1 = list(map(int, input().split()))
    mat1.append(L1)
for _ in range(r):
    L2 = list(map(int, input().split()))
    mat2.append(L2)
result = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)
for row in result:
    print(" ".join(map(str, r)))

#QUESTION 02
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(n):
    matrix[i].reverse()
for row in matrix:
    print(' '.join(map(str, row)))
#QUESTION 03
n, m= map(int, input().split())
arr = []
for i in range(n):
    L = list(map(int, input().split()))
    arr.append(L)
maxi = arr[0][0]
for i in arr:
    for j in i:
        if j > maxi:
            maxi = j
print(maxi)
#QUESTION 04
n = int(input())
arr = []
for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
symmetric = True
for i in range(n):
    for j in range(n):
        if arr[i][j] != arr[j][i]:
            symmetric = False
            break
if symmetric:
    print("Symmetric matrix")
else:
    print("Not symmetric matrix")









