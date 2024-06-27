import sys
from collections import deque
input = sys.stdin.readline
sori = deque(map(str,input().strip()))
print(sori)

duck = [[] for _ in range(500)]
cnt = 0
cur = 0
firsti, qi, ui, ai, ci = 0, 0, 0, 0, 0

while sori:
    x = sori.popleft()
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
            cnt += 1
            
        else:
            cnt = -1
            break
    print(firsti, qi, ui, ai, ci, x)
        
        
