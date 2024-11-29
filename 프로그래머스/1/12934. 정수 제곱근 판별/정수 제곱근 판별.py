import math
def solution(n):
    answer = 0
    i = int(math.sqrt(n))
    if i**2 == n:
        return (i+1)**2 
    
    return -1