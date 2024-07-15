import sys
from collections import deque
input = sys.stdin.readline
sori = deque(map(str,input().strip()))
print(sori)

duck = [[] for _ in range(500)]
cnt = 0
cur = 0
firsti, qi, ui, ai, ci = 0, 0, 0, 0, 0
sameCheck = 0
while sori:
    x = sori.popleft()

    print(duck[qi])
    if x == 'q':
        duck[firsti].append('q')
        firsti += 1
    elif x == 'u':
        if 'q' in duck[qi]:
            duck[qi].append('u')
            qi += 1
        else:
            cnt = -1
            break
    elif x == 'a':
        if 'u' in duck[ui]:
            duck[ui].append('a')
            ui += 1
        else:
            cnt = -1
            break
    elif x == 'c':
        if 'a' in duck[ai]:
            duck[ai].append('c')
            ai += 1
        else:
            cnt = -1
            break
    elif x == 'k':
        if 'c' in duck[ci]:
            duck[ci].append('k')
            ci += 1
        else:
            cnt = -1
            break
        print(firsti, qi, ui, ai, ci, x)    
        print(duck[firsti-1])
        
        if firsti == qi == ui == ai == ci:
            tmp = ['q','u','a','c','k']
            print(ci)
            if duck[ci-1] == tmp:
                if sameCheck == 0:
                    cnt += 1
                    firsti, qi, ui, ai, ci = 0, 0, 0, 0, 0
                    sameCheck = 1
                else:
                    pass
                
        else:
            cnt += 1
            sameCheck = 0



if cnt == 0:
    cnt = -1

print(cnt)
        
