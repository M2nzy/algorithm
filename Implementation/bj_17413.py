import sys
<<<<<<< HEAD

input = sys.stdin.readline

S = input()
N = len(S)
check = 0
result = []

i = 0
count = 0
while True:
    if count == N:
        break

    if S[i] == '<':
        check = 1
        checkidx = i
    elif S[i] == '>':
        result.append(S[i:checkidx:-1])
        check = 0
    elif S[i] == ' ':
        if check == 0:
            result.append(S[i::-1])
            S = S[i+1:]
            i = 0 
            continue
    
    i +=1
    count += 1
=======
input= sys.stdin.readline

S = input().strip()

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
            result += "".join(tmp[i::-1])    
            tmp = "" 
            result += " "
            first = i
    
    elif tagCheck == 0:
        tmp += S[i]


    if (i == (len(S)-1)) and (i != first):        

        result += "".join(S[i:first-1:-1])


        

>>>>>>> c022424fd890729f5530b24ffc84accfd21f944e
print(result)