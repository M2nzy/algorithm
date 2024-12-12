from collections import Counter
def solution(k, tangerine):
    tangerine.sort(reverse=True)
    a = Counter(tangerine)
    result = []
    key = list(a.items())
    key.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(key)):
        tmp = k - key[i][1]
        # 딱 맞게 귤을 뺐을 경우
        if tmp == 0:
            result.append(key[i][0])
            k -= key[i][1]
            break
        # [i][0]호에서 가지고 있는 귤이 더 많아서 빼다가 남을 경우
        elif tmp < k and tmp < 0:
            result.append(key[i][0])
            break    
        # [i][0]호에 해당하는 귤은 다 뺐지만 아직 귤이 더 필요한 경우
        elif tmp <= k:
            result.append(key[i][0])
            k -= key[i][1]
        
        
    return len(result)