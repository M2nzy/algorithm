import sys
arr = sys.stdin.readline().strip()

a = 0
b = 0
ax = 0
bx = 0
resulta = 0
resultb = 0
result = 0
for i in range(len(arr)):
    if ((arr[i] == ')') and a == 0) or ((arr[i] == ']') or b == 0):
        print(0)
        break
    else:
        if arr[i] == '(' and a==0:
            a += 1
        elif arr[i] == '[' and b==0:
            b += 1
        elif arr[i] == '(' and a!=0:
            a += 1
            ax += 1
        elif arr[i] == '[' and b!=0:
            b += 1
            bx +=1

        elif arr[i] == ')' and ax == 0:
            a -= 1
            result += 2
        elif arr[i] == ']' and bx == 0:
            b -= 1
            result += 3
        elif arr[i] == ')' and ax != 0:
            a -= 1
            result = 2*result
        elif arr[i] == ']' and bx == 0:
            b -= 1
            result = 3*result


if a != 0 or b != 0:
    print(0)    

    