def solution(s):
    answer = ''
    l = len(s)
    if l % 2 == 0:
        answer += ''.join(s[(l//2)-1])
        answer += ''.join(s[(l//2)])
    else:
        answer += ''.join(s[l//2])
    return answer