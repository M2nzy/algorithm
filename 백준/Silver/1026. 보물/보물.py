import sys 
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
S = 0

for i in range(len(B)):
    S += (min(A) * max(B))
    Aidx = A.index(min(A))
    Bidx = B.index(max(B))
    del A[Aidx]
    del B[Bidx]

print(S)