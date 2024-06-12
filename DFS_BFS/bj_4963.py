import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global q, visited,dx,dy, graph, x, y
    while(q):
        cur = q.popleft()

        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]




input = sys.stdin.readline
w, h = map(int, input().split())

x, y = 0, 0
inputGraph = []
for _ in range(h):
    inputGraph.append(input().split())

    
#len(inputGraph[0]) == 가로 길이
# len(inputGraph) == 세로 길이
graph = [[0] * (len(inputGraph[0])) for _ in range(len(inputGraph))]
visited = [[False] * len(inputGraph[0]) for _ in range(len(inputGraph))]


print(visited)
for i in range(len(inputGraph)):
    for j in range(len(inputGraph[0])):
        if inputGraph[i][j] == '1':
            
            graph[i][j] = 1
        
print(graph)


q = deque()