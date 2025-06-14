import heapq
def solution(n, words):
    answer = []
    wordsN = len(words)
    speakeds = []
    for i in range(n):
        speakeds.append([])
    i = 0
    cnt = 0
    prev = ''
    while True:
        if cnt == wordsN:
            break
        if i > (n-1):
            i = 0

        if prev == '':
            pass
        elif prev != '' and (prev[-1] != words[cnt][0]):
            answer = [(i+1), (cnt // n) + 1]
            return answer
            
        for speaked in speakeds:
            if words[cnt] in speaked:
                answer = [(i+1), (cnt // n) + 1]
                return answer
            
        heapq.heappush(speakeds[i],words[cnt])
        prev = words[cnt]
        cnt += 1
        i += 1
    
    answer = [0, 0]
    return answer