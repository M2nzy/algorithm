def solution(babbling):
    answer = 0
    speak = ["aya","ye","woo","ma"]

    for i in range(len(babbling)):
        if "ayaaya" in babbling[i]:
            continue
        if "yeye" in babbling[i]:
            continue
        if "woowoo" in babbling[i]:
            continue
        if "mama" in babbling[i]:
            continue

        if "aya" in babbling[i]:
            babbling[i] = babbling[i].replace("aya", " ")
        if "ye" in babbling[i]:
            babbling[i] = babbling[i].replace("ye", " ")
        if "woo" in babbling[i]:
            babbling[i] = babbling[i].replace("woo", " ")
        if "ma" in babbling[i]:
            babbling[i] = babbling[i].replace("ma", " ")

                
    for i in range(len(babbling)):
        if "" == babbling[i].strip():
            answer += 1
    
    return answer