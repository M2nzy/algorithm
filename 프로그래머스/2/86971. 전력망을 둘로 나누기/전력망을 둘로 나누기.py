from collections import deque
def solution(n, wires):
    resultarr = []
    answer = -1
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a, b in wires:
        # 전선들 중 하나 끊기 -> 전력망 네트워크 2개 분할
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 끊긴 각각의 곳에서 bfs 시작
        # 두개 트리 송전탑 개수 구하고
        sub1 = bfs(n, graph, a)
        sub2 = bfs(n, graph, b)
        # 차이 구하기
        resultarr.append(abs(sub1-sub2))
        
        # 간선 복구
        graph[a].append(b)
        graph[b].append(a)
        
    return min(resultarr)


def bfs(n, graph, start):
    q = deque()
    q.append(start)
    visited = [False] * (n+1)
    visited[start] = True
    count = 1
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                count += 1 
                
    return count
        
    