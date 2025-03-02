import math
def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        count = divisor(i)
        if count <= limit:
            answer += count
        else:
            answer += power
    return answer
        
def divisor(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            count += 1
            if i != (n // i):
                count += 1
                
    return count