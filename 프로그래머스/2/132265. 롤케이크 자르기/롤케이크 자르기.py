from collections import Counter
def solution(topping):
    answer = 0
    
    # 처음엔 alice가 모든 토핑 종류를 가짐
    bob = Counter()
    alice = Counter(topping)
    
    # 슬라이딩 윈도우 사용
    for t in topping:
        alice_len = len(alice)
        bob_len = len(bob)
        
        bob[t] += 1
        alice[t] -= 1
        
        if alice[t] == 0:
            del alice[t]
        
        if alice_len == bob_len:
            answer += 1
            
    return answer