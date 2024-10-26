def solution(n):
    answer = ""
    new = []
    n = str(n)
    for i in range(len(n)):
        new.append(n[i])
    new.sort(reverse=True)
        
    print(new)
    for i in range(len(new)):
        answer += ''.join(new[i])
    answer = int(answer)
    return answer