import sys

def bfs():
    global count, q, visited
    while(q):
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1,N+1):
            if not visited[next] and miro[cur][next]:
                count += 1
                visited[next] = True
                q.append(next)

N, M = map(int, sys.stdin.readline().split())

miro = [[False] * (M) for _ in range(N+1)]

print(miro)

for i in range(1,N+1):
    a = sys.stdin.readline()
    for j in range(len(a)):
        if a[j] == '1':
            miro[i][j] = True
    print(miro)

q = [1]
count = 0
visited = [False] * (N+1)
visited[1] = True

print(visited)
bfs()
print(count)