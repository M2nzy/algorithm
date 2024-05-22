import sys
N, M = map(int, sys.stdin.readline().split())
S = set()
for i in range(N):
    S.add(sys.stdin.readline().strip())


inspect = []
for i in range(M):
    inspect.append(sys.stdin.readline().strip())

count = 0
for i in range(M):
    if inspect[i] in S:
        count += 1
        continue

print(count)