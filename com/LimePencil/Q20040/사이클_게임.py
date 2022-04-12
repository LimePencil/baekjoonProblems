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
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v,m=map(int,input().split())
root = list(range(v))
ans=0
for i in range(1,m+1):
    a,b=map(int,input().split())
    if union(a,b):
        ans=i
        break
print(ans)