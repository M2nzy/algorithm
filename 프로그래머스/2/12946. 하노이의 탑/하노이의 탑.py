import sys
sys.setrecursionlimit(10000000)

# 재귀의 명사 = 하노이
def solution(n):
    answer = []
    answer = hanoi(n, 1, 3, 2)
    return answer

def hanoi(n, start, dest, via):
    if n == 1:
        return [[start, dest]]
    
    result = []
    result += hanoi(n - 1, start, via, dest)
    result.append([start, dest])
    result += hanoi(n - 1, via, dest, start)
    return result
