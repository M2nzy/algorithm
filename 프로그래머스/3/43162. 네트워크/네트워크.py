from collections import deque
def solution(n, computers):
    visited = [False] * n # 모든 노드를 단 1번만 방문해야 하므로 solution()에서 관리
    count = 0
    for i in range(n):
        if not visited[i]: # 방문하지 않았다면
            bfs(computers,n,i, visited) # 방문처리
            count += 1 
    return count

# [
#  [1, 1, 0]
#  [1, 1, 0]
#  [0, 0, 1]
# ]
def bfs(graph, n, i, visited):
    q = deque()
    q.append(i)
    count = 0 
    while q:
        x = q.popleft()
        visited[x] = True
        
        for j in range(n):
            if 0 <= j < n:
                if not visited[j] and graph[x][j] == 1: 
                    q.append(j)
                    visited[j] = True
    
    