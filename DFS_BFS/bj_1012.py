import sys
from collections import deque

def bfs():
    global q, visited, graph, count
    count = 1
    while(q):
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if (0 <= nx < N) and (0 <= ny < M):
                if (visited[nx][ny] == False) and (graph[nx][ny] == True):
                    q.append((nx, ny))
                    count += 1
                    graph[nx][ny] = False
    return count


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
T = int(input().strip())



for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False] * (N) for _ in range(M)]
    visited =[[False] * (N) for _ in range(M)]
    print(graph)
    for _ in range(K):

        X, Y = map(int, input().split())
        graph[X][Y] = True

    q = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if(graph[i][j] == True):
                q.append((i, j))
                cnt = bfs()

    print(cnt)