import sys

n, m = map(int, sys.stdin.readline().split())
person = [[1], [1]]
maze = []

for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().strip())))


def dfs(x, y, xm, yn):
    print(x, y)
    if(x == 0) and (y == 0):
        x += 1
        y += 1
        return False
    if x == -1 or y == -1 or x > xm or y > yn or (x == xm and y == yn):
        return False


    if maze[x+1][y] == 1:
        result += 1
        x += 1
    
    if maze[x][y+1] == 1:
        result += 1
        y += 1
    
    if maze[x-1][y] == 1:
        result += 1
        x -= 1
    
    if maze[x][y-1] == 1:
        result += 1
        y -= 1
    
a = 0

for i in range(n):
    for j in range(m):
        dfs(i, j, m, n)


print(a)