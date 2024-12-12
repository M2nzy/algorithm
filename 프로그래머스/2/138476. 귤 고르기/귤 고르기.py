from collections import Counter
def solution(k, tangerine):
    answer = 0
    tangerine.sort(reverse=True)
    
    heap = []
    
    a = Counter(tangerine)
    result = []
    key = list(a.items())
    key.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(key)):
        tmp = k - key[i][1]
        if tmp == 0:
            result.append(key[i][0])
            k -= key[i][1]
            break
        elif tmp < k and tmp < 0:
            result.append(key[i][0])
            break    
        elif tmp <= k:
            result.append(key[i][0])
            k -= key[i][1]

        
        
    return len(result)