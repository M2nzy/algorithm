import sys

N = int(sys.stdin.readline().strip())
T = []
P = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    T.append(a)
    P.append(b)

dp = [0 for _ in range(N+1)] # 얻을 수 있는 최대 이익

for i in range(N-1, -1, -1): # 거꾸로 돌기
    time = i + T[i] # 소요날짜
    if time > N: # 소요날짜가 퇴사일을 넘으면
        dp[i] = dp[i+1] # 최대 이익 넣기
    else:
        # 퇴사일을 안넘으면
        # 최대 이익 결과값에 (그날의 이익+소요날짜) 랑 (최대 이익) 중
        # 비교해서 더 큰거 대체해서 집어넣기
        dp[i] = max(P[i] + dp[time], dp[i+1])
print(dp[0])