import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global q, visited, graph
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if (0 <= nx < M) and (0 <= ny < N):
                if (visited[nx][ny] == False) and (graph[nx][ny] == True):
                    q.append((nx, ny))
                    graph[nx][ny] = False


input = sys.stdin.readline
T = int(input().strip())



for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False] * (N) for _ in range(M)]
    visited =[[False] * (N) for _ in range(M)]
     
    for _ in range(K):

        X, Y = map(int, input().split())
        graph[X][Y] = True

    q = deque()
    count = 0
    for i in range(M):
        for j in range(N):
            if visited[i][j] == False and graph[i][j] == True:
                q.append((i, j))
                bfs()
                count += 1

    print(count)