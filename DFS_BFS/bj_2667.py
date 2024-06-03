import sys
from collections import deque

input = sys.stdin.readline

N, M = int(input())
graph = [[False] * (N+1) for _ in range(N+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

a, b = map(int, input().split())

print(a)
print(b)    