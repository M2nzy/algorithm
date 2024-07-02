import heapq
def solution(scoville, K):
    answer = 0
    sco = []


    for i in range(len(scoville)):
        heapq.heappush(sco, scoville[i])

    while True:
        if sco[0] >= K:
            break
        elif len(sco) < 2:
            answer = -1
            break
        elif len(sco) > 1000000:
            answer = -1
            
        else:
            minSco = []
            for _ in range(2):
                minSco.append(sco[0])
                heapq.heappop(sco)

            newSco = minSco[0] + (minSco[1] * 2)
            heapq.heappush(sco, newSco)
            answer += 1
    
    
            
    
    return answer
