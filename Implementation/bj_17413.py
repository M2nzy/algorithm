import sys
input= sys.stdin.readline

S = input().strip()

print(S)
tagCheck = 0
i = 0
N = len(S)
result = ""
tagClose = 0
first = 0
tmp = ""
for i in range(len(S)):

    if S[i] == '<':
        tagStart = i
        if tmp:
            result += "".join(tmp[::-1])  
            tmp = "" 
        tagCheck = 1
        

    elif S[i] == '>':
        tagCheck = 0 
        tagClose = i
        tagLen = tagClose - tagStart
        result += "".join(S[tagStart:tagClose+1])
        first = i

    elif S[i] == ' ':
        if tagCheck == 1:
            continue
        elif tagCheck == 0: # just blank
            print(i, first)
            print("tmp:",tmp)
            result += "".join(tmp[i:(first+1):-1])    
            result += " "
            first = i
    
    elif tagCheck == 0:
        tmp += S[i]
        print(tmp)


    if (i == (len(S)-1)) and (i != first):        

        result += "".join(S[i:first-1:-1])


        

print(result)