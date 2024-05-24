import sys

N = int(sys.stdin.readline().strip(), 8)

binN = bin(int(N))

for i in range(2, len(binN)):
    print(binN[i], end='')