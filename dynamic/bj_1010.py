import sys
from itertools import combinations
T = int(sys.stdin.readline().strip())
for i in range(T):
    N,M = map(int, sys.stdin.readline().split())
    arr=[]

    for j in range((M*N)):
        arr.append(list(combinations(range(M),N)))
    

    print(len(arr))