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
v=int(input())
root = list(range(v))
edges=[]
nodes=[]
for _ in range(v):
    a,b=map(float,input().split())
    nodes.append((a,b))
for a in range(v-1):
    for b in range(a+1,v):
        x1,y1=nodes[a]
        x2,y2=nodes[b]
        edges.append((((x1-x2)**2+(y1-y2)**2)**0.5,a,b))
edges.sort()
w=0
for c,a,b in edges:
    if not union(a,b):
        w+=c
print(w)