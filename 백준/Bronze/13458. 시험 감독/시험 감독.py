import math
import sys
input = sys.stdin.readline
N = int(input().strip())
A = map(int, input().split())
B, C = map(int, input().split())

result = []
for i in A:
    if i-B < 0:
        tmp = 1
        continue
    else:
        tmp = i - B
    if tmp % C == 0:
        result.append(int(tmp / C))
        
    else:
        result.append(int(math.ceil(tmp / C)))
        
answer = 0
for i in range(len(result)):
    answer += result[i]
answer += N

print(answer)