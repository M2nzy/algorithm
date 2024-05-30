import sys

def dfs(v):
    global visited
    visited[v] = True
    print(v, end=' ')
    for next in range(1, (N+1)):
        if not visited[next] and graph[v][next]:
            dfs(next)

def bfs():
    global q, visited
    while(q):
        cur = q.pop(0)
        
        print(cur, end=' ')
        for next in range(1, (N+1)):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
        



N, M, V = map(int, sys.stdin.readline().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

# 그래프 초기화
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

dfs(V)
print()

visited = [False] * (N+1)
q = [V]
visited[V] = True

bfs()

