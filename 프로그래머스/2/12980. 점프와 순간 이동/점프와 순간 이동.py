def solution(n):
    answer = 0
    dist = 0
    while True:
        if n == 0:
            return dist
        elif (n % 2) == 0 and (n // 2) > 0:
            n //= 2
            continue
        elif (n-1) >= 0:
            n -= 1
            dist += 1
            

    return dist