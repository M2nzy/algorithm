import sys


input = sys.stdin.readline

N = int(input())
visited = [[False] * (N) for _ in range(N)]


danji = []
for _ in range(N):
    danji.append(list(input().strip()))
