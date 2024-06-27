import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))
K = int(input().strip())


tree = {}
order = list(map(int, input().split()))

order.insert(0, False)
print(order)
rootIndex = int(len(order)/2)

# root node
tree[order[rootIndex]] = [0, 0]

