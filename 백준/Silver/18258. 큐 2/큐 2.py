# import sys

# n = int(sys.stdin.readline().strip())
# arr = []
# for i in range(n):
#     arr.append(sys.stdin.readline().strip())

# queue = []

# for i in range(len(arr)):
#     if 'push' in arr[i]:
#         index = arr[i].find(' ')
#         queue.append(arr[i][index+1:])
#     elif 'pop' in arr[i]:
#         if not queue:
#             print("-1")
#         elif queue:
#             print(queue[0])
#             del queue[0]

#     elif 'size' in arr[i]:
#         print(len(queue))
#     elif 'empty' in arr[i]:
#         if not queue:
#             print("1")
#         else:
#             print("0")
#     elif 'front' in arr[i]:
#         if not queue:
#             print("-1")
#         elif queue:
#             print(queue[0])
#     elif 'back' in arr[i]:
#         if not queue:
#             print("-1")
#         elif queue:
#             print(queue[-1])

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

queue = deque()

for i in range(len(arr)):
    if 'push' in arr[i]:
        index = arr[i].find(' ')
        queue.append(arr[i][index+1:])
    elif 'pop' in arr[i]:
        if not queue:
            print("-1")
        elif queue:
            print(queue.popleft())

    elif 'size' in arr[i]:
        print(len(queue))
    elif 'empty' in arr[i]:
        if not queue:
            print("1")
        else:
            print("0")
    elif 'front' in arr[i]:
        if not queue:
            print("-1")
        elif queue:
            print(queue[0])
    elif 'back' in arr[i]:
        if not queue:
            print("-1")
        elif queue:
            print(queue[-1])

    