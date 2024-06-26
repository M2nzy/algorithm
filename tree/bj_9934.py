import sys
input = sys.stdin.readline

K = int(input().strip())


tree = {}
order = list(map(int, input().split()))

order.insert(0, False)
print(order)
for i in range(1, int((len(order)+1)/2)):
    tree[order[i+1]] = [order[i], order[i+2]]



print(tree)

# DFS 돌렸을때 출력되는 순서를 반대로
