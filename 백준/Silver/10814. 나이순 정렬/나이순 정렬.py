import sys

n = int(sys.stdin.readline().strip())
persons = []
for i in range(n):
    age, name = list(sys.stdin.readline().strip().split())
    cnt = i
    persons.append([int(age), name, cnt])

persons.sort(key=lambda x:(x[0], x[2]))
for p in persons:
    print(p[0], p[1])