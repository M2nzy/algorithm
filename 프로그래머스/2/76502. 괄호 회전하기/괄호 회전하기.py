from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    
    for i in range(len(s)):
        flag = 0
        stack = []
        for cur in s:
            if not stack:
                if cur == ']' or cur == '}' or cur == ')':
                    flag = -1
                    break
                else: 
                    stack.append(cur)
            else:
                if (stack[-1] == '[' and cur == ']') or (stack[-1] == '{' and cur == '}') or (stack[-1] == '(' and cur == ')'):
                    stack.pop()
                else:
                    stack.append(cur)
                    
        if not stack and not flag == -1:
            answer += 1
        s.rotate(-1)
    return answer