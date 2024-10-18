import heapq
def solution(book_time):
    answer = 0
    time = []
    book_time.sort()
    for i in range(len(book_time)):
        s = toMin(book_time[i][0])
        e = toMin(book_time[i][1])
        time.append([s,e])
    
    time.sort()
    
    heap =[]
    
    for i in range(len(time)):
        if not heap:
            e = (time[i][1])+10
            heapq.heappush(heap, e)        
        elif heap[0] <= time[i][0]:
            heapq.heappop(heap)
            e = (time[i][1])+10
            heapq.heappush(heap, e)     
        else:
            e = (time[i][1])+10
            heapq.heappush(heap, e)     
        
        
    return len(heap)

def toMin(time):
    h, m = map(int, time.split(":"))
    return (h*60) + m