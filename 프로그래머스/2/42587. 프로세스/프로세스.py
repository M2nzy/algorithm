from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    prioritiesName = deque()
    
    for i in range(len(priorities)):
        prioritiesName.append('num'+str(i)) # 타겟 이름 배열을 새로 만들어줌
        
    count = 0
    target = prioritiesName[location] # 타겟 이름 저장
    
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
        
        elif maxPrior == cur: # 우선순위가 가장 높지만 타겟이 아닐 경우 (우선순위가 동일한 프로세스)
            count += 1 # 실행은 하지만 리턴은 하지 않음
            continue
            
        else: # 우선순위가 높지도 않고 타겟도 아닐 경우 다시 큐에 넣기
            priorities.append(cur)
            prioritiesName.append(curName)
