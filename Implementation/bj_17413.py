import sys

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
print(result)