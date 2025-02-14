def solution(phone_number):
    answer = ''
    l = len(phone_number) - 4
    star = '*' * l
    answer += ''.join(star)
    answer += ''.join(phone_number[l:])
    return answer