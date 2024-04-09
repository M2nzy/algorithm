import sys
n = int(sys.stdin.readline().strip())
move = list(map(str,sys.stdin.readline().split()))
Ax = 1
Ay = 1

for i in range(len(move)):
    if move[i] == 'L':
        if (Ay - 1) == 0:
            continue
        else:
            Ay -= 1
    elif move[i] == 'R':
        if (Ay + 1) > n:
            continue
        else:
            Ay += 1
    elif move[i] == 'U':
        if (Ax - 1) == 0:
            continue
        else:
            Ax -= 1
    elif move[i] == 'D':
        if (Ax + 1) > n:
            continue
        else:
            Ax += 1
    
print(Ax, Ay)