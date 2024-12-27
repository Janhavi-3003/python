mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
row= 0
col = 0
diag = 0
m = 3
n = 3
for j in range(0, n-1):
    row += mat[0][j]
for j in range(0, n-1):
    row += mat[1][j]
for i in range(0, m):
    col += mat[i][n-1]
for i in range(0, m):
    for j in range(0, n):
        if ((i + j) == (m - 1)):
            diag += mat[i][j]
        if(j == 0 and i == m-1):
            col -= mat[i][j]
sum = diag + row + col
print("Sum of Zig-Zag pattern is ", sum)
