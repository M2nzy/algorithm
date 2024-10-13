def solution(s):
    answer = True
    length = len(s)
    if length != 4 and length != 6:
        return False
    for i in range(len(s)):
        if s[i].isalpha():
            return False 
            
    return answer