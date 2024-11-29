from itertools import combinations
def solution(numbers):
    answer = []
    comb = list(combinations(numbers,2))
    
    num = []
    for i in range(len(comb)):
         num.append(sum(comb[i]))
            
    answer = list(set(num))
    answer.sort()
    return answer