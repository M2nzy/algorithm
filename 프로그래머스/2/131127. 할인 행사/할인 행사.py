from collections import deque
def solution(want, number, discount):
    answer = 0
    start = 0
    end = 10
    
    want_dict = dict()
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    while True:
        cur = discount[start:end]
        
        if start == end: break
        if end > len(discount): break
        if start > end: break
        
        disc_dict = dict()
        for i in range(len(cur)):
            disc_dict[cur[i]] = 0
        for i in range(len(cur)):
            disc_dict[cur[i]] += 1

        flag = -1
        for item in want_dict:
            if disc_dict.get(item) == None:
                flag = -1
                break
            if disc_dict.get(item) < want_dict[item]:
                flag = -1
                break
            else:
                flag = 1

        if flag == 1:
            answer += 1
        
        end += 1
        start += 1
        
    return answer