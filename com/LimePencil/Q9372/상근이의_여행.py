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
for _ in range(int(input())):
    v,e=map(int,input().split())
    root = list(range(v+1))
    edges=[]
    for _ in range(e):
        a,b=map(int,input().split())
        edges.append((a,b))
    edges.sort()
    w=0
    for a,b in edges:
        if not union(a,b):
            w+=1
    print(w)

# 트리 정의로 쉬운 풀이

# import sys

# input = sys.stdin.readline
# for _ in range(int(input())):
#     v,e=map(int,input().split())
#     for _ in range(e):
#         a,b=map(int,input().split())
#     print(v-1)