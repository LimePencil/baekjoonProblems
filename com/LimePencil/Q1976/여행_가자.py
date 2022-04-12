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
m=int(input())
root = list(range(v))
planets= [list(map(int,input().split())) for _ in range(v)]

for i in range(v-1):
    for j in range(i,v):
        if planets[i][j] ==1:
            union(i,j)

route=list(map(int,input().split()))
ans="YES"
for i in range(len(route)-1):
    if find(route[i]-1) != find(route[i+1]-1):
        ans="NO"
        break
print(ans)