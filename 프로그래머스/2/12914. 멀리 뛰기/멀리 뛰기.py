def solution(n):
    result = 0
    fibo = [1, 2]
    if n == 1:
        return 1
    if n >= 2:
        for i in range(2, n):
            a = fibo[i-1] + fibo[i-2]
            fibo.append(a)
        result = fibo[-1] % 1234567
    
    return result
