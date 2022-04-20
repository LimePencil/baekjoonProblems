import sys
import math

def lazy_update(node,start,end):
    if lazy[node] !=0:
        tree[node] = (end-start+1)-tree[node]
        if start!=end:
            lazy[node*2] ^=1
            lazy[node*2+1] ^=1
        lazy[node] = 0


def lazy_range(node, start,end,left,right):
    lazy_update(node,start,end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] = (end-start+1)-tree[node]
        if start != end:
            lazy[node*2] ^=1
            lazy[node*2+1] ^= 1
        return
    lazy_range(node*2,start,(start+end)//2,left,right)
    lazy_range(node*2+1,(start+end)//2+1,end,left,right)
    tree[node] = tree[node*2] + tree[node*2+1]

def find_sum(node,start,end,left,right):
    lazy_update(node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return find_sum(node*2,start,(start+end)//2,left,right) +find_sum(node*2+1,(start+end)//2+1,end,left,right)

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [0]*tree_depth
lazy = [0]*tree_depth
for _ in range(m):
    l = list(map(int,input().split(" ")))
    if l[0] == 0:
        lazy_range(1,0,n-1,l[1]-1,l[2]-1)
    else:
        print(find_sum(1,0,n-1,l[1]-1,l[2]-1))