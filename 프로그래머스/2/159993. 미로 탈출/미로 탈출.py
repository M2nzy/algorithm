from collections import deque
def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    a1 = []
    a2 = []
    for i in range(N):
        a1.append(list(maps[i]))
        a2.append(list(maps[i]))
            
    visited1 = [[False] * M for _ in range(N)]
    visited2 = [[False] * M for _ in range(N)]

    answer = bfs1(a1, visited1)
    if type(answer) == str:
        return -1
    elif answer <= 0:
        return -1
    else:
        answer2 = bfs2(a2, visited2)
        if type(answer2) == str:
            return -1
        elif answer2 <= 0:
            return -1
        else:
            return answer2 + answer


def bfs1(maps, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()  
    N = len(maps)
    M = len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                tmp = (i, j)
                maps[i][j] = 0
                q.append(tmp)
                break
            
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and (maps[nx][ny] == 'L'):
                    maps[nx][ny] = int(maps[x][y]) + 1
                    return maps[nx][ny]
                elif not visited[nx][ny] and ((maps[nx][ny] == 'O') or (maps[nx][ny] == 'E') or (maps[nx][ny] == 'S')):
                    q.append((nx, ny))
                    maps[nx][ny] = int(maps[x][y]) + 1
    return -1
                    
                    
                   
            
            
def bfs2(maps, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()  
    N = len(maps)
    M = len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'L':
                tmp = (i, j)
                maps[i][j] = 0
                q.append(tmp)
                break
            
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and (maps[nx][ny] == 'E'):
                    maps[nx][ny] = int(maps[x][y]) + 1
                    return maps[nx][ny]
                elif not visited[nx][ny] and ((maps[nx][ny] == 'O') or (maps[nx][ny] == 'L') or (maps[nx][ny] == 'S')):
                    q.append((nx, ny))
                    maps[nx][ny] = int(maps[x][y]) + 1
                    
    return -1
                    