import sys

n = int(sys.stdin.readline().rstrip("\n"))
tree = {}

def preorder(p):
    print(p,end="")
    if tree[p][0] != ".":
        preorder(tree[p][0])
    if tree[p][1] != ".":
        preorder(tree[p][1])
    pass
def inorder(p):
    if tree[p][0] != ".":
        inorder(tree[p][0])
    print(p,end="")
    if tree[p][1] != ".":
        inorder(tree[p][1])
    pass
def postorder(p):
    if tree[p][0] != ".":
        postorder(tree[p][0])
    if tree[p][1] != ".":
        postorder(tree[p][1])
    print(p,end="")
    pass

for _ in range(n):
    p,l,r = sys.stdin.readline().rstrip("\n").split(" ")
    tree[p] = (l,r)

preorder("A")
print()
inorder("A")
print()
postorder("A")

