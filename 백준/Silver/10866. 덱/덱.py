import sys
from collections import deque

n = int(sys.stdin.readline().strip())
command = []
for i in range(n):
    command.append(sys.stdin.readline())
deq = deque()
tmp = []
for i in range(len(command)):
    if "push_front" in command[i]:
        deq.appendleft(command[i].split()[1])
    elif "push_back" in command[i]:
        deq.append(command[i].split()[1])
    elif "pop_front" in command[i]:
        if not deq:
            print("-1")
        else:
            print(deq[0])
            del deq[0]
    elif "pop_back" in command[i]:
        if not deq:
            print("-1")
        else:
            print(deq[-1])
            del deq[-1]
    elif "size" in command[i]:
        print(len(deq))
    elif "empty" in command[i]:
        if not deq:
            print("1")
        else:
            print("0")
    elif "front" in command[i]:
        if not deq:
            print("-1")
        else:
            print(deq[0])
        
    elif "back" in command[i]:
        if not deq:
            print("-1")
        else:
            print(deq[-1])
        