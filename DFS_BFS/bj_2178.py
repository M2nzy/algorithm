import sys
from collections import deque


def bfs():
    global q, visited
    while(q):
        cur = q.pop(0)
        visited[cur] = True
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                q.append(next)
                bfs()



input = sys.stdin.readline
N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

inputMiro = []
miro = []
q = []
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N):
    inputMiro.append(input().strip())

print(inputMiro)
for i in range(N):
    miro.append(list(inputMiro[i]))
print(miro)