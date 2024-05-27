import sys
import copy
S = sys.stdin.readline().strip()
St = copy.deepcopy(S)

arr = []
if '<' in St:

    indexLeft = St.find('<')
    indexRight = St.find('>')
    arr.append(St[:indexRight+1])
    St = St[indexRight+1:]
    while(True):     

        indexLeft = St.find('<')
        indexRight = St.find('>')
        if indexRight == -1:
            break
        else:
            arr.append(St[:indexLeft])
            arr.append(St[indexLeft:indexRight+1])
            St = St[indexRight+1:]
    

else:
    arr = St.split()

print(arr)

for i in arr:
    if '<' in i:
        print(i, end='')    
    else:
        if ' ' in i:
            a = i.split(' ')
            print(a)
            for j in range(len(a)):
                for k in range(1, (len(a[j])+1)):
                    print(a[j][-k], end='')
                if j == len(a):
                    print('', end='')
                else:
                    print(' ', end='')
        else:
            for j in range(1, (len(i)+1)):
                print(i[-j],end='')
    if '<' in S:
        print('',end='')
    else:
        print(' ',end='')