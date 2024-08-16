def solution(s):
    answer = ''
    s = s.lower()
    
    flag = 0
    for i in range(len(s)):
        if i==0:
            answer += s[i].upper()
        elif s[i] == ' ' and flag == 0:
            flag = 1
            answer += s[i]
            
        elif flag == 1 and s[i].isdigit():
            answer += s[i]
            flag = 0
            
        elif flag == 1 and s[i].isalpha():
            answer += s[i].upper()
            flag = 0
            
        else:
            answer+=s[i]
        
    return answer