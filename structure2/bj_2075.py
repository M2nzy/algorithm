import heapq
import sys

N = int(sys.stdin.readline().strip())
heap = []

for i in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    if len(heap) < N:
        heapq.heappush(heap, numbers[i])
    else:
        if numbers[i] > heap[0]:
            continue
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, numbers[i])
    
print(heap)