from collections import deque 
def solution(begin, target, words):
    answer = 0
    # hit -> cog로 가는 길 찾기
    if target not in words:
        return 0
    words.sort()
    return bfs(begin, target, words)

def bfs(begin, target, words):
    q = deque()
    n = len(begin)
    visited = dict()
    
    for word in words:
        visited[word] = False
    q.append((begin, 0))
    
    while q:
        cur, dist = q.popleft()
        visited[begin] = True
        
        if cur == target:
            return dist
        
        for word in words:
            difCnt = 0
            for i in range(n):
            # 한개의 알파벳을 바꾸고 검증하는 방법
                if cur[i] != word[i]:
                    difCnt += 1
                    continue   

            if difCnt == 1 and visited[word] == False:
                q.append((word, dist+1))
                visited[word] = True
                break
        
    
    return dist