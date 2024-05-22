import sys
from collections import deque

ball = deque()

N = int(sys.stdin.readline().strip())
seq = deque(map(int,sys.stdin.readline().split()))
    
for i in range(N):
    ball.append(i+1)


for i in range(N):
    print(ball[0], end=' ')

    index = seq[0]
    del ball[0]
    del seq[0]
    if index > 0:
        
        index -= 1
        ball.rotate(-index)
        seq.rotate(-index)
    else:        
        
        ball.rotate(-index)
        
        
        seq.rotate(-index)
    