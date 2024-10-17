def solution(brown, yellow):
    answer = []
    by = brown + yellow
    if yellow == 1:
        return [3,3]
    for i in range(3, by):
        for j in range(3, by):
            if i >= j:
                mul = i * j
                if mul == by and ((i-2)*(j-2)) == yellow:
                    answer.append(i)
                    answer.append(j)
                    return answer
                else:
                    continue
            else:
                break
    
    
    return answer
