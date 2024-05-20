import sys
import heapq
N = int(sys.stdin.readline().strip())
c = []
for i in range(N):
    c.append(int(sys.stdin.readline().strip()))
x = []
for i in range(N):
    if c[i] == 0:
        if not x:
            print(0)
        else:
            print(-heapq.heappop(x))
            # index = x.index(maxx)
            # del x[index]
    else:
        heapq.heappush(x, -c[i])