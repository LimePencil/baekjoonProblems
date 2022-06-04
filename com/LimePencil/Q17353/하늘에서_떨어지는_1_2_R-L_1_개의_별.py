import sys
import math


def lazy_update(node,start,end):
    if lazy[node] !=0:
        tree[node] += (end-start+1)*lazy[node]
        if start!=end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0


def lazy_range(node, start,end,left,right,value):
    lazy_update(node,start,end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1)*value
        if start!=end:
            lazy[node*2] += value
            lazy[node*2+1] += value
        return
    lazy_range(node*2,start,(start+end)//2,left,right,value)
    lazy_range(node*2+1,(start+end)//2+1,end,left,right,value)
    tree[node] = tree[node*2] + tree[node*2+1]

def find_sum(node,start,end,left,right):
    lazy_update(node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return find_sum(node*2,start,(start+end)//2,left,right) +find_sum(node*2+1,(start+end)//2+1,end,left,right)

input = sys.stdin.readline
n=int(input())
arr = [0]+list(map(int,input().split()))
m=int(input())
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [0]*tree_depth
lazy = [0]*tree_depth
for i in range(1,n+1):
    lazy_range(1,1,n,i,i,arr[i]-arr[i-1])
for _ in range(m):
    l = list(map(int,input().split()))
    if l[0] == 2:
        a,b=l
        print(find_sum(1,1,n,1,b))
    else:
        a,b,c=l
        lazy_range(1,1,n,b,c,1)
        lazy_range(1,1,n,c+1,c+1,-(c-b+1))