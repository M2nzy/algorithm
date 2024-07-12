def solution(prices):
    count = []
    priceLen = len(prices)
    for _ in range(priceLen):
        count.append(0)
    
    for i in range(priceLen):
        for j in range(i+1, priceLen):
            #같으면 유지
            if prices[i] == prices[j]:
                count[i] += 1
            #올랐으면 초 증가
            elif prices[i] < prices[j]:
                count[i] += 1
            #떨어진거면 유지 초 센 후 카운트 그만
            elif prices[i] > prices[j]:
                count[i] += 1
                break
                
    return count