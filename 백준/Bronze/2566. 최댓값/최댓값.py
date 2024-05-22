import sys
arr = []
for i in range(9):
    arr.append(list(map(int,sys.stdin.readline().split())))

max = 0
maxX = 1
maxY = 1
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            maxX = i + 1
            maxY = j + 1

print(max)
print(maxX, maxY)