import sys
N, M = map(int, sys.stdin.readline().split())
poketmon = []
poketmonInput = []
for i in range(N):
    poketmonInput.append(sys.stdin.readline().strip())

for i, content in enumerate(poketmonInput):
    poketmon.append((i+1, content))
 
poketmon = dict(poketmon)
reverse_poketmon = {v:k for k,v in poketmon.items()}

command = []
for i in range(M):
    command.append(sys.stdin.readline().strip())
    if command[i].isalpha():
        print(reverse_poketmon.get(command[i]))

    else:
        print(poketmon.get(int(command[i])))