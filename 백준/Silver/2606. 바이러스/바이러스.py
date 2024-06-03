import sys
input = sys.stdin.readline

count = 0
def BFS():
    global q,count, visited
    
    while(q):
        if q[0] == 1:
            count = 0
        else: count += 1
        cur = q.pop(0)
        visited[cur] = True
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                q.append(next)
                BFS()



N = int(input())

L = int(input())


graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(L):
    x, y = map(int, input().split())    
    graph[x][y] = graph[y][x] = True


visited[1] = True
q = [1]
BFS()
print(count)