from collections import deque 
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost = deque(lost)
    reserve = deque(reserve)
    count = 0
    answer = n - len(lost)
    rmv_lost = []
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                del reserve[j]
                rmv_lost.append(lost[i])
                count += 1
                break
    for i in range(len(rmv_lost)):
        lost.remove(rmv_lost[i])

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if not reserve:
                break
            elif ((lost[i]-1) == reserve[j]) or ((lost[i]+1) == reserve[j]):
                count += 1
                del reserve[j]
                break
            else:
                continue
    answer += count
    return answer