from collections import deque
def solution(n, edge):
    answer = 0
    # 간선리스트 -> 인접리스트로 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 1부터 탐색하게 하여 모든 노드 탐색해서 각 노드의 거리 저장
    distances = bfs(n, graph, 1)
    mn = max(distances)
    # 가장 먼 노드일 경우
    for dist in distances:
        if dist == mn:
            answer += 1
    return answer

def bfs(n, graph, start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
        
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = visited[cur] + 1   
                
    return visited
