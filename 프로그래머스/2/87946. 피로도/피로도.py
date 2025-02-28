
def solution(k, dungeons):
    global answer
    answer = 0
    
    cnt = []
    visited = [False] * len(dungeons)
    for i in range(len(dungeons)):
        answer = (dfs(k, i, dungeons, visited, 0))
    return answer

# k 현재 피로도
# i 몇번째 던전

def dfs(k, i, dungeons, visited, cnt):
    global answer
    
    answer = max(cnt, answer)
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and k >= dungeons[i][1] and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], i, dungeons, visited, cnt+1)
            visited[i] = False
    return answer