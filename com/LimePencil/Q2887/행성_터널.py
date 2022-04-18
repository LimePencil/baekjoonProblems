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
for i in range(v):
    a,b,c=map(float,input().split())
    nodes.append((i,a,b,c))
nodes.sort(key= lambda x:x[1])
for a in range(v-1):
    idx1,x1,y1,z1=nodes[a]
    idx2,x2,y2,z2=nodes[a+1]
    edges.append((abs(x1-x2),idx1,idx2))
nodes.sort(key= lambda x:x[2])
for a in range(v-1):
    idx1,x1,y1,z1=nodes[a]
    idx2,x2,y2,z2=nodes[a+1]
    edges.append((abs(y1-y2),idx1,idx2))
nodes.sort(key= lambda x:x[3])
for a in range(v-1):
    idx1,x1,y1,z1=nodes[a]
    idx2,x2,y2,z2=nodes[a+1]
    edges.append((abs(z1-z2),idx1,idx2))  
edges.sort()
w=0
for c,a,b in edges:
    if not union(a,b):
        w+=c
print(int(w))