def solution(friends, gifts):
    answer = 0
    f = {}
    friends.sort()
    gifts.sort()
    for i in range(len(friends)):    
        f[friends[i]] = 0
    
    # f: 선물지수 완료
    for i in range(len(gifts)):
        cur = gifts[i].split(' ')
        for j in range(2):
            if j == 0:
                f[cur[j]] += 1
            elif j == 1:
                f[cur[j]] -= 1
    

    # 이차원 배열로? 가로에서 비교하기
    biao = [[0] * (len(friends)) for _ in range(len(friends))]

    for i in range(len(friends)):
        for k in range(len(gifts)):
            cur = gifts[k].split(' ')
            if cur[0] == friends[i]:
                for j in range(len(friends)):
                    if cur[1] == friends[j]:
                        biao[i][j] += 1
                        break
    a = []
    for i in range(len(friends)):
        a.append(0)
    for i in range(len(biao)):
        for j in range(len(biao)):
            if (biao[i][j] == biao[j][i]):
                if f[friends[i]] > f[friends[j]]:
                    a[i]+=1
                elif f[friends[i]] < f[friends[j]]:
                    a[i] += 1
                    a[j] += 1
                elif f[friends[i]] == f[friends[j]]:
                    break
                else:
                    break
            elif biao[i][j] > biao[j][i]:
                a[i] += 1
            elif biao[i][j] < biao[j][i]:
                a[j] += 1
            else:
                break
    a.sort()
    answer = a[-1]
    return answer