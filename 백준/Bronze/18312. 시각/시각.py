import sys
N, K= map(int, sys.stdin.readline().split())
clock = []

hour = 0
minute = 0
second = 0
for i in range(N+1):
    if(i < 10):
        hour = "0" + str(i)
    else:
        hour = str(i)

    for j in range(60):
        if(j < 10):
            minute = "0" + str(j)
        else:
            minute = str(j)
            
        for k in range(60):
            if(k < 10):
                second = "0" + str(k)
            else:
                second = str(k)

            if str(K) in hour:
                current = str(hour)+str(minute)+str(second)
                clock.append(current)
            
            elif str(K) in minute:
                current = str(hour)+str(minute)+str(second)
           

                clock.append(current)
            elif str(K) in second:
                current = str(hour)+str(minute)+str(second)
            
                clock.append(current)

print(len(clock))