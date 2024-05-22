import heapq
import sys
N = int(sys.stdin.readline().strip())
arr = []
absarr = []
arr2 = []
for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x != 0:
        heapq.heappush(arr, x)
        heapq.heappush(arr2, abs(x))
    else:
        if not arr:
            print(0)
        else:
            if abs(arr[0]) in arr:
                heapq.heappop(arr)
        
print(printarr)