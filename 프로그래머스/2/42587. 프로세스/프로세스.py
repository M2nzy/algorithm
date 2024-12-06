from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    prioritiesName = deque()
    
    for i in range(len(priorities)):
        prioritiesName.append('num'+str(i))
        
    count = 0
    
    target = prioritiesName[location]
    while True:
        if not priorities:
            break
        if not prioritiesName:
            break
            
        maxPrior = max(priorities) # 현재 가장 우선순위가 높은 프로세스
        cur = priorities.popleft()
        curName = prioritiesName.popleft()
        
        if maxPrior == cur and target == curName: # 우선순위가 가장 높고 타겟일 경우
            count += 1
            return count
        
        elif maxPrior == cur:
            count += 1
            continue
            
        else:
            for i in range(len(priorities)):
                if cur < priorities[i]:
                    priorities.append(cur)
                    prioritiesName.append(curName)
                    break
