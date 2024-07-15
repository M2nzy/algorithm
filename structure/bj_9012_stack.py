import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    S = input().strip()

    stack = []
    for i in range(len(S)):
        
        if S[i] == ')':
            if not stack:
                stack = -1
                break
            else:
                stack.pop()
        elif S[i] == '(':
            stack.append(S[i])
            

    if not stack:
        print("YES")
    else:
        print("NO")    