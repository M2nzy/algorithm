#입력받은 시간 정렬 후
#앞시간 + 현재시간
import sys
n =  int(input())
time = [int(sys.stdin.readline().strip()) for i in range(n)]

time.sort()
print(time)