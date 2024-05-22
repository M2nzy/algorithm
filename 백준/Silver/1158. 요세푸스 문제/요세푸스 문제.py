import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
arr = deque()
for i in range(1,n+1):
    arr.append(i)

k -= 1
print("<", end='')
for i in range(len(arr)):
    arr.rotate(-(k))
    

    if len(arr)==1:
        print(arr[0], end=">")
    else:
        print(arr[0],end=", ")
    del arr[0]

    
    