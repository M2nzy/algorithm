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
    
    # 전체적인 방향
    # 인덱스 0을 지웠으니까 왼쪽으로 회전을 시켜야함

    # 이미 0번째를 지웠으니까 왼쪽으로 한번 더 당겨주기
    if index > 0:
        index -= 1
        ball.rotate(-index)
        seq.rotate(-index)
    
    # 음수일 때는 오른쪽이라 당기지 않아도 됨
    else:        
        ball.rotate(-index)
        seq.rotate(-index)
    