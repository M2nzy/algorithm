from collections import deque
import math
def solution(arr):
    answer = 0
    l = 0
    g = 0
    r = 0
    arr = deque(arr)

    for i in range(len(arr)-1):
        if not r:
            g = math.gcd(arr[i], arr[i+1])
            l = arr[i] * arr[i+1] // g
            r = l
        elif r:
            g = math.gcd(r, arr[i+1])
            l = r * arr[i+1] // g
            r = l
        
    
    
    return r