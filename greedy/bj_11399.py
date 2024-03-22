#입력받은 시간 정렬 후
#현재 리스트 요소까지 전부 더하기
import sys
n = int(sys.stdin.readline())
time = list(map(int,sys.stdin.readline().split()))
result = 0
time.sort()
print("time:",time)

for i in range(n):
    # While문
    # j = 0
    # while(True):
    #     if(j==i+1):
    #         break
    #     else:
    #         result += time[j]
    #         j += 1
        
    for j in range(i+1):
        result += time[j]

print(result)