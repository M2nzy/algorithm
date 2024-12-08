import itertools
def solution(clothes):
    answer = 0
    zhong = dict()
    # 키 마다 빈 값의 딕셔너리 생성
    for i in range(len(clothes)):
        zhong[clothes[i][1]] = list()
        
    # 각 키에 리스트 아이템들 할당
    for i in range(len(clothes)):
        zhong[clothes[i][1]] += [clothes[i][0]]
        
    # 옷 종류 몇개인지 구하기
    a = len(zhong)
    result = 1
    
    # 옷 종류가 여러개일 경우
    if a > 1:
        for i in zhong: 
            # (그 종류 내용물에 따라 입을 수 있는 총 가지수 구하기(len) + 이 종류를 안 입는 경우 1개)
            # => 종류별로 모두 곱하기
            result *= (len(zhong[i]) + 1)
        answer = (result - 1) # 아예 모든 것을 아무것도 안 입는 경우 빼기
        return answer
    
    # 옷 종류가 1개일 경우
    elif a == 1:
        for i in zhong: # 옷 하나씩 더하기
            result *= len(zhong[i])
        answer = result
        return answer
    else: # 무의미
        return 1