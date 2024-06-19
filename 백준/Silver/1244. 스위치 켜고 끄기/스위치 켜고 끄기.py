import sys

input = sys.stdin.readline
N = int(input().strip())

switch = list(map(int, input().split()))
student = int(input().strip())

# 계산하기 편하게 맨 앞에 쓸모없는 거 추가
switch.insert(0, False)

for _ in range(student):
    info, switchNum = map(int, input().split())
    
    if info == 1: #남자
        for i in range(1, N+1):
            if i % switchNum == 0:
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0

    elif info == 2: #여자
        if switch[switchNum] == 1:
            switch[switchNum] = 0
        elif switch[switchNum] == 0:
            switch[switchNum] = 1


        for i in range(1, N+1):
            if ((switchNum - i) > 0) and ((switchNum + i) <= (N)):
                if switch[(switchNum - i)] != switch[(switchNum + i)]:   
                    break                
                else:
                    if switch[(switchNum - i)] == 0:
                        switch[(switchNum - i)] = 1
                        switch[(switchNum + i)] = 1
                    else:
                        switch[(switchNum - i)] = 0
                        switch[(switchNum + i)] = 0


for i in range(1, N+1):
    print(switch[i], end=' ')

    if i % 20 == 0:
        print()

if N % 20 != 0:
    print()