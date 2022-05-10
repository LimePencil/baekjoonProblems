import sys
import math
import bisect

def find_kth(node, start, end, left,right,kth):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return bisect.bisect_left(tree[node],kth)
    return find_kth(2*node,start,(start+end)//2,left,right,kth) + find_kth(2*node+1,(start+end)//2+1,end,left,right,kth)

def change_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    tree[node].append(value)
    if start!=end:
        change_tree(2*node,start,(start+end)//2,index,value)
        change_tree(2*node+1,(start+end)//2+1,end,index,value)

input = sys.stdin.readline
n,m = list(map(int,input().split()))
arr=list(map(int,input().split()))
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [[] for _ in range(tree_depth)]
for i in range(len(arr)):
    change_tree(1,0,n-1,i,arr[i])
for i in range(len(tree)):
    tree[i].sort()
for _ in range(m):
    i,j,k = list(map(int,input().split()))
    l=-1000000000
    r=1000000000
    while l<=r:
        mid=(l+r)//2
        x=find_kth(1,0,n-1,i-1,j-1,mid)
        if x<k:
            l=mid+1
        else:
            r=mid-1
    print(l-1)