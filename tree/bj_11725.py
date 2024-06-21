import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global q, visited, graph

    while q:
        cur = q.popleft()
        visited[cur] = True
        for next in range(N+1):
            if not visited[next] and graph[cur][next]:
                q.append(next)
                
def dfs(v):
    global visited, result,graph
    visited[v] = True
    result.append(v)
    for next in range(N+1):
        if not visited[next] and graph[v][next]:
            dfs(next)




N = int(input().strip())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range (N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

q = deque()
q.append(1)
result = []
dfs(1)

print(result)