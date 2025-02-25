from collections import deque
import sys

def bfs(n, maps, i, j):
    q = deque()
    q.append((i, j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * (n) for _ in range(n)]
    count = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        maps[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    maps[nx][ny] = 0
                    count += 1

    return count

n = int(sys.stdin.readline().strip())
global maps
maps = []
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().strip())))
                
answer = []
cnt = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            r = bfs(n, maps, i, j)
            cnt += 1
            answer.append(r)

print(cnt)
answer.sort()
for i in answer:
    print(i)