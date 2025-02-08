from collections import deque
def solution(numbers, target):
    return bfs(numbers, target)


def bfs(numbers, target):
    q = deque()
    cnt = 0
    start = 0
    n = len(numbers)
    q.append((start + numbers[0], 0))
    q.append((start - numbers[0], 0))
    
    while q:
        cur, dist = q.popleft()
        
        if cur == target and dist == n-1:
            cnt += 1
        
        if (dist+1) < n:
            pnx = cur + numbers[(dist+1)]
            mnx = cur - numbers[(dist+1)]
            q.append((pnx, dist+1))
            q.append((mnx, dist+1))
            
            
    return cnt