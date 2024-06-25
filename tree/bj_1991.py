import sys
input = sys.stdin.readline
N = int(input().strip())


tree = {} 

for _ in range(N):
    x, y, z = map(str, input().split())
    tree[x] = y, z


