import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
def bfs():
    global q, visited, danji
    cnt = 1
    while(q):
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if (visited[nx][ny] == False) and (danji[nx][ny] == '1'):
                    q.append((nx, ny))
                    danji[nx][ny] = 0
                    cnt += 1
    return cnt



N = int(input())
visited = [[False] * (N) for _ in range(N)]

tmp = []

danji = []
for _ in range(N):
    danji.append(list(input().strip()))

q = deque()
answer = []

for i in range(N):
    for j in range(N):
        if danji[i][j] == '1':
            q.append((i,j))
            answer.append(bfs())            

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])