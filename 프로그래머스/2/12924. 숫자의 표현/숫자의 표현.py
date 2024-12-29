def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        answer += maken(i, n)
    return answer

def maken(start, n):
    r = 0
    for i in range(start, n+1):
        r += i
        if r == n:
            return 1
        if r > n:
            return 0
    return 0