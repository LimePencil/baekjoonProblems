import sys

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return True
    else:
        root[a]=b
        return False

def find(node):
    if root[node] != node:
        root[node] = find(root[node])
    return root[node]

input = sys.stdin.readline
n,m=map(int,input().split())
root = list(range(n))
edges=[]
nodes=[]
already_connected = [[False]*n for _ in range(n)]
for _ in range(n):
    a,b=map(int,input().split())
    nodes.append((a,b))
for _ in range(m):
    a,b=map(int,input().split())
    already_connected[a-1][b-1] =True
    already_connected[b-1][a-1] =True
for a in range(n-1):
    for b in range(a+1,n):
        x1,y1=nodes[a]
        x2,y2=nodes[b]
        if already_connected[a][b]:
            edges.append((0,a,b))
        else:
            edges.append((((x1-x2)**2+(y1-y2)**2)**0.5,a,b))
edges.sort()
w=0
for c,a,b in edges:
    if not union(a,b):
        w+=c
print("{:.2f}".format(w))