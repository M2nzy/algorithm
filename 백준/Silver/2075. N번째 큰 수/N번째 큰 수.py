import sys
import heapq

N = int(sys.stdin.readline().strip())
heap = []
numbers = []
for i in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if not heap:
            heapq.heappush(heap, numbers[j])

        elif numbers[j] >= heap[0]:
            if len(heap) >= N:
                heapq.heappop(heap)
                heapq.heappush(heap, numbers[j])

            else:
                heapq.heappush(heap, numbers[j])
        else:
            continue
    
print(heap[0])
