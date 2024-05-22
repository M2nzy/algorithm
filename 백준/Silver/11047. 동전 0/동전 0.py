import sys
n,k = map(int,input().split())
count = 0
a = [int(sys.stdin.readline().strip()) for i in range(n)]
listidx = -1
while True:
    mox, nameji = divmod(k, a[listidx])
    if(mox == 0):
        if(nameji <= 0):
            break
        elif(a[listidx] == a[0]):
            if(mox > 0):
                count += mox
            break
        else:
            listidx -= 1
            continue
    elif(mox > 0):
        count += mox
        k -= (a[listidx]*mox)
        listidx -= 1

    if(nameji <= 0):
            break    

print(count)   
