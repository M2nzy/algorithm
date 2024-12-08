import math
def solution(citations):
    answer = 0
    citations.sort()
    
    harray = []
    for i in range(len(citations)):
        h = i+1
        shang = 0
        xia = 0
        for j in range(len(citations)):
            if citations[j] >= h:
                shang += 1
            if citations[j] <= h:
                xia += 1
        if xia <= h <= shang:
            harray.append(h)
    if not harray:
        return 0
    return max(harray)