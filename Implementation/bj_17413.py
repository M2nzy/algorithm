import sys
import copy
S = sys.stdin.readline().strip()
St = copy.deepcopy(S)

answer = []
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
            arr.append(St[0:])
            break
        else:
            arr.append(St[:indexLeft])
            arr.append(St[indexLeft:indexRight+1])
            St = St[indexRight+1:]
    

else:
    arr = St.split()


for i in arr:

    if '<' in i:
#        print(i, end='')    
        answer.append(i)
    else:
        if (' ' in i) and ('<' not in i):
            
            a = i.split(' ')
            for j in range(len(a)):
                for k in range(1, (len(a[j])+1)):
  #                      print(a[j][-k], end='')
                        answer.append(a[j][-k])
                if j+1 == len(a):
 #                   print('', end='')
                    answer.append('')
                else:
#                    print(' ', end='')
                    answer.append(' ')
        else:
            for j in range(1, (len(i)+1)):
#                print(i[-j],end='')
                answer.append(i[-j])
    if '<' in S:
#        print('',end='')
        answer.append('')
    else:
#        print(' ',end='')
        answer.append(' ')

answer.reverse()
for i in range(len(answer)):
    if answer[0] == '':
        answer.pop(0)
    elif answer[0] == ' ':
        answer.pop(0)
    else:
        break
answer.reverse()

for i in range(len(answer)):
    print(answer[i], end='')