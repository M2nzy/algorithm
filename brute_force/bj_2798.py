import sys

N, M = map(int, sys.stdin.readline().split())
card = []

cardResult = []
result = 0
card = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result += card[i]
            result += card[j]
            result += card[k]
            cardResult.append(result)
            result = 0

result = 0    
cardResult.sort(reverse=True)
for i in range(len(cardResult)):
    if cardResult[i] > M:
        continue
    else:
        result = cardResult[i]
        break
print(result)
