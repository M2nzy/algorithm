import heapq
import sys
N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if not arr:
            print(0)
        else:
<<<<<<< HEAD
            if abs(arr[0]) in arr:
                heapq.heappop(arr)
=======
            print(heapq.heappop(arr)[1])


    
                        
>>>>>>> a8017c56529a4507a4c069fefb764adec4eabad4
