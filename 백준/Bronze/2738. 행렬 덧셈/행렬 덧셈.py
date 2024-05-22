import sys
n, m = map(int, sys.stdin.readline().split())

arrA = []
arrB = []
arrC = []

for i in range(n):
    arrA.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    arrB.append(list(map(int, sys.stdin.readline().split())))
# 2차원 배열 초기화
arrC = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arrC[i][j] = arrA[i][j] + arrB[i][j]

for i in range(n):
    for j in range(m):
        if j == range(m-1):
            print(arrC[i][j], end="")
    
        else:
            print(arrC[i][j], end=" ")
    print("")