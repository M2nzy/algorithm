import sys
<<<<<<< HEAD
from itertools import combinations
T = int(sys.stdin.readline().strip())
for i in range(T):
    N,M = map(int, sys.stdin.readline().split())
    arr=[]

    for j in range((M*N)):
        arr.append(list(combinations(range(M),N)))
    

    print(len(arr))
=======
from itertools import combinations, permutations
T = int(sys.stdin.readline().strip())
for i in range(T):
    N,M = map(int, sys.stdin.readline().split())


    comb = list(combinations(range(N), M))
    print(comb)
>>>>>>> 5eb77835124a78235a7b94eeedc407bea98f6f45
