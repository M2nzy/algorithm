import itertools
def solution(clothes):
    answer = 0
    zhong = dict()
    
    for i in range(len(clothes)):
        zhong[clothes[i][1]] = list()
    for i in range(len(clothes)):
        zhong[clothes[i][1]] += [clothes[i][0]]

    a = len(zhong)
    result = 1
    if a > 1:
        for i in zhong: # 종류에 따라 더하기
            result *= (len(zhong[i]) + 1)
        answer = (result - 1)
        return answer
    elif a == 1: # 옷 종류가 1개뿐
        for i in zhong: # 옷 하나씩 더하기
            result *= len(zhong[i])
        answer = result
        return answer
    else:
        return 1