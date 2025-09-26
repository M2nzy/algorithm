from collections import deque
from itertools import permutations

def solution(elements):
    n = len(elements)
    arr = []
    element = deque(elements)
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr.append(slidesum(j, element))
        element.rotate(-1)
        
    arr = set(arr)
    return len(arr)

def slidesum(i, element):
    temp = list(element)
    temp = temp[:i]
    return sum(temp)
