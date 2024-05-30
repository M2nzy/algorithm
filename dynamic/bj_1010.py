import sys
from itertools import combinations, permutations
T = int(sys.stdin.readline().strip())
for i in range(T):
    N,M = map(int, sys.stdin.readline().split())


    comb = list(combinations(range(N), M))
    print(comb)