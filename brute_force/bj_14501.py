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
dayResult = 0

i = 0
while(True):
    dayResult += T[i]
    i = T[i]
