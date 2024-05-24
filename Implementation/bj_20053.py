import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    N = int(sys.stdin.readline().strip())
    
    num = (list(map(int, sys.stdin.readline().split())))

    print(min(num), max(num))