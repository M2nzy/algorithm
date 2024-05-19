import sys
from collections import deque

testcase = int(sys.stdin.readline().strip())

important = []
for i in range(testcase):
    n, m = map(int, sys.stdin.readline().split())
    importants = list(map(int, sys.stdin.readline().split()))
    # init deque
    q = deque()
    for j, important in enumerate(importants):
        q.append((j, important))


    importants.sort(reverse=True)
    count = 1

    for i in range(n):
        print("q:",q)
        print("importants:",importants)
        if importants[0] == q[i][1]: 
            if q[i][0] == m:
                print(count)
                break
            else:
                
                q.rotate(-1)
                count += 1

        else:
            count += 1
            q.rotate(-1)