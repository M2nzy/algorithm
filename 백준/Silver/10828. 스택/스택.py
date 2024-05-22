import sys

n = int(sys.stdin.readline().strip())
command = []
for i in range(n):
    command.append(sys.stdin.readline().strip())

stack = []
for i in range(len(command)):
    if 'push' in command[i]:
        index = command[i].find(' ')
        stack.append(command[i][index+1:])
    if 'pop' in command[i]:
        if not stack:
            print('-1')
        else:
            print(stack.pop())
    if 'size' in command[i]:
        print(len(stack))

    if 'empty' in command[i]:
        if not stack:
            print('1')
        elif stack:
            print('0')

    if 'top' in command[i]:
        if not stack:
            print('-1')
        else: print(stack[-1])
