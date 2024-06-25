import sys
input = sys.stdin.readline
N = int(input().strip())



def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


tree = {}

for _ in range(N):
    x, y, z = map(str, input().split())
    tree[x] = y, z

preorder('A')
print()
inorder('A')
print()
postorder('A')