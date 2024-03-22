#입력받은 시간 정렬 후
#앞시간 + 현재시간
import sys
n = int(input())
time = list(map(int,sys.stdin.readline().split()))
result = 0
time.sort()

def selfsum(a):
    if a <= 1:
        return a
    return a + selfsum(a-1)

for i in range(n):
    result += selfsum(time[i])
    print(result)

print(result)