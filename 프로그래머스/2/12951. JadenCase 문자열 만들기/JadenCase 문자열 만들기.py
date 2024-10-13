def solution(s):
    answer = ''
    string = s.split(' ')
    length = len(string)
    a = 0
    for i in string:
        answer += i.capitalize()
        if a == length-1:
            break
        answer += ' '
        a += 1
        
    return answer