import sys

N = sys.stdin.readline().strip()

number = int(N)
minNum = int(N)-(int(len(N))*9)    
numLen = int(len(N))

a = []
for i in str(number):
    a.append(int(i))
print(a)

while(True):
    