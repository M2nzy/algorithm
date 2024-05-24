import sys
A,B,C,M = map(int, sys.stdin.readline().split())

work = 0
pirodo = 0
for i in range(24):
    if (pirodo + A) > M:
        pirodo -= C
        if pirodo < 0:
            pirodo = 0
    else:    
        work += B
        pirodo += A

print(work)