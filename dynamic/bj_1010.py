import sys
input = sys.stdin.readline

T = int(input().strip())


for i in range(T):
    dp = []
    N, M = map(int, input().split())
    
    for j in range(M):
        if j == 0:
            dp.append(1)
        else:
            dp.append(dp[j-1] * j)
    
    print(dp)

    top = dp[M-1]
    bottom = dp[(M-N-1)] * dp[N-1]
    print(int(top/bottom))