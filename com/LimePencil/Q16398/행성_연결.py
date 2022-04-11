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
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
v=int(input())
root = list(range(v))
edges=[]
planets= [list(map(int,input().split())) for _ in range(v)]

for i in range(v-1):
    for j in range(i,v):
        edges.append((planets[i][j],i,j))
edges.sort()

w=0
for c,a,b in edges:
    if not union(a,b):
        w+=c
print(w)