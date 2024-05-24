import sys

N = int(sys.stdin.readline().strip())

TP = []
for i in range(N):
    TP.append(list(map(int, sys.stdin.readline().split())))
T = []
P = []
for i in range(len(TP)):
    T.append(TP[i][0])
    P.append(TP[i][1])

reward = 0
day = 0
dayarr = []
for i in range(N):
    for j in range(N):

        day += T[i] 


    if day > N:
        break 
    
    