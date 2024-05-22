import sys

def recursion(s, l, r, cnt):
    if l >= r:
        cnt+=1
        return 1, cnt
    elif s[l] != s[r]:
        cnt+=1
        return 0, cnt
    else: return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

T = int(sys.stdin.readline().strip())
S = []
for i in range(T):
    S.append(sys.stdin.readline().strip())


for i in range(T):
    result = isPalindrome(S[i])
    print(result[0], result[1])