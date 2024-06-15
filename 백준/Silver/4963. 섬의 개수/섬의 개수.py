import sys
from collections import deque

dy = [-1, 1, 0, 0, 1, -1, 1, -1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]
def bfs():
    count = 1
    global q, visited,dx,dy, graph
    while(q):
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    count += 1
    return count

while(True):
    input = sys.stdin.readline
    w, h = map(int, input().split())
    if (w == 0 and h == 0):
        break
    inputGraph = []
    for _ in range(h):
        inputGraph.append(input().split())

        
    graph = [[0] * (w) for _ in range(h)]
    visited = [[False] * (w) for _ in range(h)]


    for i in range(h):
        for j in range(w):
            if inputGraph[i][j] == '1':
                graph[i][j] = 1


    q = deque()
    result = 0
    for i in range(h):
        for j in range(w):
            if(graph[i][j] == 1):
                q.append((i,j))
                tmp = bfs()
                if tmp > 0:
                    result += 1

    print(result)