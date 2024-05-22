import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    printer = deque()
    important = deque(sys.stdin.readline().split())

    for j in range(N):
        printer.append(j+1)
    
    a = -1
    cnt = 0
    a = printer[M]
    for j in range(N):

        print("a:",a)
        maxI = important.index()
        print(maxI)
        maxx = max(important)

        if maxx == a:
            printer.popleft()
            important.popleft()
            cnt += 1
            print(cnt)
        else:
            printer.rotate(-1)
            important.rotate(-1)
