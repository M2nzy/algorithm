import sys
n = int(sys.stdin.readline())
time = list(map(int,sys.stdin.readline().split()))
result = 0
time.sort()
for i in range(n):
 
        
    for j in range(i+1):
        result += time[j]

print(result)