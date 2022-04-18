from collections import defaultdict
import sys

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        root[a]=b
        number[b]+=number[a]

def find(node):
    if root[node] != node:
        root[node] = find(root[node])
    return root[node]

input = sys.stdin.readline
for _ in range(int(input())):
    f=int(input())
    root=defaultdict(str)
    number=defaultdict(int)
    for _ in range(f):
        a,b=input().split()
        if a not in root:
            root[a]=a
            number[a]=1
        if b not in root:
            root[b]=b
            number[b]=1
        union(a,b)
        print(number[find(a)])