import sys
input = sys.stdin.readline

A, B = map(int, input().split())
result = 0

S = []
S.append(False)
for i in range(1, 1001):
    for _ in range(i):
        S.append(i)

for i in range(A, B+1):
    result += S[i]

print(result)