import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    important = list(map(int, sys.stdin.readline().split()))

    iq = deque()
    for i in range(N):
        iq.append((i, important[i]))

    count = 0
    while(True):
        maxx = max(important)        
        if (maxx == iq[0][1]):
            if(iq[0][0] == M):
                count +=1
                print(count)
                break
            else:
                important.remove(maxx)
                iq.rotate(-1)
                count +=1
                
            
        else:
            iq.rotate(-1)
