import sys


N, M, V = map(int, sys.stdin.readline().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[b][a] = graph[a][b] = True

print(graph)

