import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)  
def dfs(v):
    global visited , graph
    for next in graph[v]:
        if not visited[next]:
            visited[next] = v
            dfs(next)




N = int(input().strip())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range (N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

dfs(1)
    
for i in range(2, N+1):
    print(visited[i])