import sys
from collections import deque

testcase = int(sys.stdin.readline().strip())

for i in range(testcase):
    q = deque()
    n, m = map(int, sys.stdin.readline().split())
    important = deque(map(int, sys.stdin.readline().split()))
    # init deque
    for j in range(n):
        q.append(j)

    cnt = 1
    while True:
        if important[0] == max(important):
            if q[0] == m:
                print(cnt)
                break
            else:
                q.popleft()
                important.popleft()
                cnt += 1
        else:
            q.rotate(-1)
            important.rotate(-1)