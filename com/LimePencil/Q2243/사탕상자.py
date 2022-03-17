import sys
from math import log2, ceil

def update(node,start,end,idx,diff):
    if idx<start or idx>end:
        return
    tree[node] += diff
    if start!= end:
        update(2*node,start,(start+end)//2,idx,diff)
        update(2*node+1,(start+end)//2+1,end,idx,diff)

def find(node,start,end,value):
    if start == end:
        return start
    if tree[node*2]>=value:
        return find(node*2,start,(start+end)//2,value)
    else:
        return find(node*2+1,(start+end)//2+1,end,value-tree[node*2])


input = sys.stdin.readline
tree = [0]*(2**(ceil(log2(1000000))+1))
n = int(input())
for _ in range(n):
    l = list(map(int,input().split(" ")))
    if l[0] == 1:
        a,b = l
        index = find(1,1,1000000,b)
        print(index)
        update(1,1,1000000,index,-1)
    else:
        a,b,c = l
        update(1,1,1000000,b,c)