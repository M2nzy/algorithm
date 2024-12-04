import math
def solution(n, m):
    answer = []
    a = math.gcd(n,m)
    b =((n*m) / a)
    answer = [a,b]
    return answer