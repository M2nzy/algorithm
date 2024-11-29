from collections import Counter
def solution(s):
    answer = []

    for i in range(len(s)):
        a = s[i]
        plag = 0
        for j in range(i-1, -1, -1):
            if s[j] == a and plag == 0:
                answer.append(i-j)
                plag = 1
                break
            
        if plag == 0:
            answer.append(-1)
        
    return answer