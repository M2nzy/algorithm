def solution(s):
    bincnt = 0
    totalZerocnt = 0
    while s != "1":
        zerocnt = 0
        for i in s:
            if i == "0":
                zerocnt += 1
        bincnt += 1
        totalZerocnt += zerocnt

        s = str(bin(len(s) - zerocnt))[2:]
    
    answer = [bincnt, totalZerocnt]
    
    return answer