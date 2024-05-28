import sys
import operator

T = int(sys.stdin.readline().strip())


for t in range(T):
    
    N, K = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    arr = [(0,0)]
    num.sort()
    for i in range(N):
        for j in range(N):
            arr.append((num[i], num[j]))

    list1 = sorted(arr, key=operator.itemgetter(0,1))
    print(list1[K][0]+list1[K][1])
    print(list1)
