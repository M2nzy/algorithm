def solution(sequence, k):
    if k in sequence:
        tmp = sequence.index(k)
        return [tmp, tmp]
    
    answer = [0, len(sequence)]
    
    start = 0
    end = 0
    hap = 0
    
    while end < len(sequence):

        if hap == k:
            if (answer[1] - answer[0]) > (end - start - 1):
                answer = [start, end-1]
                
            hap -= sequence[start]
            start += 1
            
        elif hap > k:
            hap -= sequence[start]
            start += 1
            
        else:
            hap += sequence[end]
            end += 1
            
    while hap >= k and start < len(sequence):
        if hap == k and (answer[1] - answer[0]) > (end - start - 1):
            answer = [start, end - 1]
        hap -= sequence[start]
        start += 1
        
    return answer