n = int(input())
cnt = 0
result = []
for i in range(n):
    arr = [list(map(int,input().split()))]
    result.append(arr)
    print(result)
    if(i==0):
        continue
    elif(result[i-1][1] > result[i][0]):
        result.pop()
    else:
        cnt += 1

    print("arr[i-1][1]:",result[i-1][1])
    print("arr[i][0]",result[i][0])
print(arr)

# 3차원 배열을 2차원으로 바꿔야함
# 들어오는 앞자리 요소를 원래 있는 리스트랑 전부 비교해서 겹치는게 있으면 받지말고