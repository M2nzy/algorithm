<<<<<<< HEAD
import sys
from collections import deque
input = sys.stdin.readline

count = 0 

def bfs():
    global q, visited, count
    while(q):
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if (visited[nx][ny] == False) and (miro[nx][ny] == '1'):
                    q.append((nx, ny))
                    count += 1
                    visited[nx][ny] = True
                    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
visited = [[False] * (M) for _ in range(N)]

miro = []
for _ in range(N):
    tmp = input().strip()
    miro.append(list(tmp))

q = deque()
q.append((0,0))
bfs()

print(count)
=======
import math
import sys
input = sys.stdin.readline
N = int(input().strip())
A = map(int, input().split())
B, C = map(int, input().split())

result = []
for i in A:
    if i-B < 0:
        tmp = 1
        continue
    else:
        tmp = i - B
    if tmp % C == 0:
        result.append(int(tmp / C))
        
    else:
        result.append(int(math.ceil(tmp / C)))
        
answer = 0
for i in range(len(result)):
    answer += result[i]
answer += N

print(answer)
>>>>>>> 7fff87f9cc625f2077c64a29b6169ac0290af63b
