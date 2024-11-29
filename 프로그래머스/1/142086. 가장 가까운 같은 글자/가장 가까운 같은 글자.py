from collections import Counter
def solution(s):
    answer = []

    for i in range(len(s)):
        a = s[i]
        flag = 0
        for j in range(i-1, -1, -1):
            if s[j] == a and flag == 0:
                answer.append(i-j)
                flag = 1
                break
            
        if flag == 0:
            answer.append(-1)
        
    return answer