import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    answer = ""
    S = input().strip().split(' ')
    for i in S:
        answer += "".join(i[::-1])
        answer += " "
    print(answer)