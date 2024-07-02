import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    #for i in range(len(scoville)):
    #    heapq.heappush(sco, scoville[i])

    while True:
        if scoville[0] >= K:
            break
        elif len(scoville) < 2 or len(scoville) > 1000000:
            answer = -1
            break
        else:
            minSco = []
            for _ in range(2):
                minSco.append(scoville[0])
                heapq.heappop(scoville)

            newSco = minSco[0] + (minSco[1] * 2)
            heapq.heappush(scoville, newSco)
            answer += 1
    
    return answer
