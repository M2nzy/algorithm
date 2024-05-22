import sys
n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

for i in range(n):
    plag = 0
    for j in range(len(arr[i])):
        if (arr[i][0] == ")") or (arr[i][-1] == "(") or (plag < 0 and arr[i][j]):
            plag = -1
            break
        else:
            if arr[i][j] == '(':
                plag += 1
                continue
            else:
                plag -= 1
                continue
    if plag == 0:
        print("YES")
    else:
        print("NO")


