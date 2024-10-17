def solution(answers):
    answer = []
    alen = len(answers)
    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]  
        
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(alen):
        if answers[i] == supoja1[i % len(supoja1)]:
            cnt1+=1 
        if answers[i] == supoja2[i % len(supoja2)]:
            cnt2+=1 
        if answers[i] == supoja3[i % len(supoja3)]:
            cnt3+=1
    
    result = []
    result.append(cnt1)
    result.append(cnt2)
    result.append(cnt3)
    m = max(result)
    for i in range(3):
        if(result[i] == m):
            answer.append(i+1)
    return answer