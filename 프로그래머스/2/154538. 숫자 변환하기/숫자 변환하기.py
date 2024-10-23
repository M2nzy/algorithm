from collections import deque
def solution(x, y, n):
    answer = 0
    answer = bfs(x,y,n)
    return answer
    
# x->y로 가는 최단 거리 구하기 
def bfs(x, y, n):
    q = deque() 
    q.append((x, 0))
    visited = set()
    visited.add(x)
    if x == y:
        return 0
    while q:
        x, dist = q.popleft()
        visited.add(x)
        for nx in ((x+n),(x*2), (x*3)):
            if nx == y:
                return dist+1
            
            if(1<= nx <= y) and nx not in visited:
                visited.add(nx)
                q.append((nx, dist+1))
    
    return -1