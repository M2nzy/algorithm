import sys

N, M, V = map(int, sys.stdin.readline().split())

#그래프 초기화
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

#정점 번호 입력받기
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

def dfs(v):
    visited[v] = True
    print(v,end=' ')
    for next in range(1, (N+1)):
        if not visited[next] and graph[v][next]:
            dfs(next)    

def bfs():
    global q, visited
    while(q):
        current = q.pop(0)

        print(current, end=' ')
        for next in range(1, (N+1)):
            if not visited[next] and graph[current][next]:
                visited[next] = True
                q.append(next)

dfs(V)
print()

visited = [False] * (N+1)
q = [V]
visited[V] = True
bfs()