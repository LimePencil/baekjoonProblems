import sys
import math
import bisect

def find_sum(node, start, end, left,right,kth):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return len(tree[node]) - bisect.bisect_left(tree[node],kth+1)
    return find_sum(2*node,start,(start+end)//2,left,right,kth) + find_sum(2*node+1,(start+end)//2+1,end,left,right,kth)

def change_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    tree[node].append(value)
    if start!=end:
        change_tree(2*node,start,(start+end)//2,index,value)
        change_tree(2*node+1,(start+end)//2+1,end,index,value)

input = sys.stdin.readline
n = int(input())
arr = []
arr=list(map(int,input().split()))
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [[] for _ in range(tree_depth)]
for i in range(len(arr)):
    change_tree(1,0,n-1,i,arr[i])
for i in range(len(tree)):
    tree[i].sort()
m = int(input())
for _ in range(m):
    i,j,k = list(map(int,input().split()))
    print(find_sum(1,0,n-1,i-1,j-1,k))