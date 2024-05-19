from itertools import product
import sys
testcase = int(sys.stdin.readline().strip())


for i in range(testcase):
    N, M = map(int, sys.stdin.readline().split())
    arr = []
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()
    result = list(product(arr, repeat=2))
 
    result.sort(key=lambda x:(x[0], x[1]))
    print(result)


    print(result[M][0]+result[M][1])