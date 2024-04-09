import sys
n, m = map(int,sys.stdin.readline().split())

#import math
#print(math.gcd(n,m))
#print(math.lcm(n,m))

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