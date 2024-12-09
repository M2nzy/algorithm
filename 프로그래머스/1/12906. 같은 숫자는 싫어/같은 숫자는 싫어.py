from collections import deque
def solution(arr):
    answer = []
    arr = deque(arr)
    while arr:
        a = arr.popleft()
        if answer:
            if answer[-1] == a:
                continue
            else:
                answer.append(a)
        elif not answer:
            answer.append(a)
    return answer
