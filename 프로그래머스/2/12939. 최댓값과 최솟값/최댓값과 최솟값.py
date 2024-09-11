def solution(s):
    answer = ''
    a = s.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    maxx = max(a)
    minn = min(a)
    
    answer = str(minn)+" "+str(maxx)
        
    return answer