def solution(n):
    answer = ''
    a = "수"
    b = "박"
    for i in range(n):
        if(i%2==0):
            answer += ''.join(a)
        else:
            answer += ''.join(b)
            
    return answer