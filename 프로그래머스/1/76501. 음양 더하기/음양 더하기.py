def solution(absolutes, signs):
    answer = 0
    index = 0
    for sign in signs:
        if sign:
            answer += absolutes[index]
        else:
            answer -= absolutes[index]
        index += 1
    return answer