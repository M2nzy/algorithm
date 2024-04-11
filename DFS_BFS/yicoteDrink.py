import sys
n, m = map(int, sys.stdin.readline().split())
box = []
result = 0


for i in range(n):
    box.append(list(map(int,sys.stdin.readline().strip())))
    
    # M 가로 길이 검증
    if len(box[i]) > m:
        exit()

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if box[x][y] == 0:
        print("x,y",x,y)
        box[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
