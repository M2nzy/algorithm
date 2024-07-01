def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    
    numbers.sort(key=lambda x:x*4, reverse = True)

    if numbers[0] == '0':
        answer = '0'
    else:
        
        answer = ''.join(numbers)
    
    
    return answer