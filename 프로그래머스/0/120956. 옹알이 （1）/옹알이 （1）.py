import itertools
def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    speak.sort()
    babbling.sort()
    iter = []
    new =[]
    
    for i in range(len(speak)):
        print(speak[i])
        new.append(speak[i])
        
    for i in range(2,5):
        iter += (list(itertools.permutations(speak,i)))

    iter.sort()
    for i in range(len(iter)):
        str = "".join(iter[i])
        new.append(str)
        
    for i in range(len(babbling)):
        if babbling[i] in new:
            answer+=1    
        
    return answer
#순열을 뽑아서 그게 문자열이 되는지 확인해야되나?