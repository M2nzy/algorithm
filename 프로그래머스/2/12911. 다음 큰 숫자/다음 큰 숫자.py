from collections import Counter
def solution(n):
    nc = Counter(bin(n)[2:])
    while True:
        n += 1
        tc = Counter(bin(n)[2:])
        if tc['1'] == nc['1']:
            break
            
    return n