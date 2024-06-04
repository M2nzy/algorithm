import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global q, visited
    while(q):
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                if (visited[nx][ny] == False) and (miro[nx][ny] == '1'):
                    q.append((nx, ny))
                    miro[nx][ny] = int(miro[x][y]) + 1
                    
    return miro[N-1][M-1]

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
print(bfs())
