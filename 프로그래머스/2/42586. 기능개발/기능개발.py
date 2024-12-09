from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    result = deque()
    while progresses:
        cur = progresses.pop() 
        curSpeed = speeds.pop()
        count = 0
        while cur < 100:
            cur += curSpeed
            count += 1
        if cur >= 100:
            result.append(count)
            
    # result가 반대로 되어있음
    tmp = []
    while result:
        if not tmp:
            cur = result.pop()
            tmp.append(cur)
        else:
            cur = result.pop()
            if cur <= tmp[0]:
                tmp.append(cur)
            else:
                answer.append(len(tmp))
                tmp = []
                tmp.append(cur)
        
    if tmp:
        answer.append(len(tmp))
        
    return answer