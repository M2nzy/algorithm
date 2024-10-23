import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    heap = []
    mixSco = 0
    count = 0
    if len(scoville) < 2 or len(scoville) > 1000000:
        return -1
    
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])

    while True:
        if not heap:
            return -1
        elif heap[0] >= K:
            break
        elif heap[0] > 1000000000 or heap[0] < 0:
            return -1
        
        else:
            if heap:
                a = heapq.heappop(heap)
            if heap:
                b = heapq.heappop(heap)
            elif not heap:
                return -1
            mixSco = a + (b * 2)        
            count += 1
            heapq.heappush(heap, mixSco)
    return count
