import sys
from collections import deque

n = int(sys.stdin.readline().strip())
info = []
important = []
for i in range(n):
    info.append(sys.stdin.readline().split())
    important.append(sys.stdin.readline().split())

print(info)
print(important)

plag = 0
q = deque()
for i in range(len(info[plag][0])):
    q.append(i)

print(q)