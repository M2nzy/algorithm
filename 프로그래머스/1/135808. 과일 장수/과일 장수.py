from collections import deque
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    score = deque(score)
    box = []
    while True:
        if len(score) < m:
            break
        tmp = []
        for i in range(m):
            x = score.popleft()
            tmp.append(x)
        box.append(tmp)
        
    if not box: return 0
    for b in box:
        answer += min(b) * len(b)
    return answer