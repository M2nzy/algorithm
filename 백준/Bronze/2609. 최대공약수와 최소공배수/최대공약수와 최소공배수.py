import sys
n, m = map(int,sys.stdin.readline().split())
gcd = 0
n1, m1 = n, m
while(True):
    if n % m == 0:
        gcd = m
        break
    else:
        tmp = n % m
        n = m
        m = tmp
        continue

print(gcd)
print(int(n1*m1/gcd))