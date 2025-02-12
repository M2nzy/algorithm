from collections import deque
def solution(s):
    s = deque(s)
    stack = deque()
    
    for i in s:
        if not stack:
            stack.append(i)
            continue
        
        if stack[-1] == i:
            stack.pop()
            continue
        
        stack.append(i)
              
    if not stack:
        return 1
    
    return 0