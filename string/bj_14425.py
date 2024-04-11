import sys
n, m = map(int, sys.stdin.readline().split())

S = set()
testStr = []

for i in range(n):
    S.append(sys.stdin.readline().strip())

for i in range(m):
    testStr.append(sys.stdin.readline().strip())

cnt = 0
for i in range(n):
    for j in range(m):
        if S[i] == testStr[j]:
            cnt += 1

print(cnt)