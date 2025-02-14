def solution(s):
    answer = ''
    stack = []
    index = 0
    for i in range(len(s)):
        if s[i] == ' ':
            stack.append(s[i])
            index = 0
        else:
            if index % 2 == 0:
                stack.append(s[i].upper())
            else:
                stack.append(s[i].lower())
            index += 1
    for i in stack:
        answer += ''.join(i)
        
    return answer