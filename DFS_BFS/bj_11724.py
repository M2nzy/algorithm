import sys
from collections import deque
def bfs():
    global q, visited, graph
    
    while q:
        cur = q.popleft()
        visited[cur] = True
        for next in range(N+1):
            if not visited[next] and graph[cur][next]:
                q.append(next)
                



input = sys.stdin.readline
N, M = map(int, input().split())


graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)


for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = True

count = 0
 
q = deque()
for i in range(N):
    for j in range(N):
        q.append(i,j)
        bfs()
        count += 1