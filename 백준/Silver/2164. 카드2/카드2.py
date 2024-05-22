import sys
from collections import deque
n = int(sys.stdin.readline().strip())

a = deque()

for i in range(n):
    a.append(i+1)


for i in range(n-1):
    del a[0]
    a.rotate(-1)
    

print(a[0])