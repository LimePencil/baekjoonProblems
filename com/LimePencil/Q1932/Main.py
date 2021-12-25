import sys

n = int(sys.stdin.readline().rstrip("\n"))
tree = []

for i in range(n):
    line = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    tree.append(line)
for a in range(n-1,0,-1):
    for b in range(0,a):
        tree[a-1][b] += max(tree[a][b],tree[a][b+1])
print(tree[0][0])

