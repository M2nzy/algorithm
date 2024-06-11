import sys
from collections import deque
def bfs():
    global q, visited, graph, cnt
    while q:
        cur = q.popleft()
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next] == True:
                visited[next] = True
                q.append(next)
                cnt -= 1




input = sys.stdin.readline
N, M = map(int, input().split())


graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)


for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = True

count = 0
q = deque()
cnt = 0
result = 0
cnt += N
for i in range(1,N+1):
    
    q.append(i)
    visited[i] = True
    bfs()
print(cnt)