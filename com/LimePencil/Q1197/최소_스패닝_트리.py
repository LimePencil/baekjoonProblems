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
v,e=map(int,input().split())
root = list(range(v+1))
edges=[]
for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort()

w=0
for c,a,b in edges:
    if not union(a,b):
        w+=c
print(w)