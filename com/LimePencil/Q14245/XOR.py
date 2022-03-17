import sys
import math

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start+end)//2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = tree[node*2] ^ tree[node*2+1]

def lazy_update(node,start,end):
    if lazy[node] !=0:
        tree[node] ^= ((end-start+1)%2)*lazy[node]
        if start!=end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0


def lazy_range(node, start,end,left,right,value):
    lazy_update(node,start,end)
    if left > end or right < start:
        return tree[node]
    if left <= start and end <= right:
        tree[node] ^= ((end-start+1)%2)*value
        if start != end:
            lazy[node*2] ^= value
            lazy[node*2+1] ^= value
        return tree[node]
    mid = (start+end)//2
    tree[node] = lazy_range(node*2,start,mid,left,right,value)^ lazy_range(node*2+1,mid+1,end,left,right,value)
    return tree[node]

def find_xor(node,start,end,idx):
    lazy_update(node,start,end)
    if idx<start or idx>end:
        return 0
    if start == end:
        return tree[node]
    mid = (start+end)//2
    return find_xor(node*2,start,mid,idx) ^ find_xor(node*2+1,mid+1,end,idx)

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [0]*tree_depth
lazy = [0]*tree_depth
init(1,0,n-1)
m = int(input())
for _ in range(m):
    l = list(map(int,input().split()))
    if l[0] == 1:
        a,b,c,d = l
        lazy_range(1,0,n-1,b,c,d)
    else:
        a,b = l
        print(find_xor(1,0,n-1,b))