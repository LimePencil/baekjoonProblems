import sys
import math

def init_min(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
    else:
        init_min(node*2, start, (start+end)//2)
        init_min(node*2+1, (start+end)//2+1, end)
        tree_min[node] = min(tree_min[node*2],tree_min[node*2+1])

def init_max(node, start, end):
    if start == end:
        tree_max[node] = arr[start]
    else:
        init_max(node*2, start, (start+end)//2)
        init_max(node*2+1, (start+end)//2+1, end)
        tree_max[node] = max(tree_max[node*2],tree_max[node*2+1])

def find_min(node, start, end, left,right):
    if left>end or right<start:
        return float('inf')
    if left<=start and end<=right:
        return tree_min[node]
    return min(find_min(2*node,start,(start+end)//2,left,right), find_min(2*node+1,(start+end)//2+1,end,left,right))

def find_max(node, start, end, left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree_max[node]
    return max(find_max(2*node,start,(start+end)//2,left,right), find_max(2*node+1,(start+end)//2+1,end,left,right))

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
arr = [int(input()) for _ in range(n)]
tree_min = [0]*2**(math.ceil(math.log2(n))+1)
tree_max = [0]*2**(math.ceil(math.log2(n))+1)
init_min(1,0,n-1)
init_max(1,0,n-1)
for _ in range(m):
    a,b = list(map(int,input().split(" ")))
    print(find_min(1,0,n-1,a-1,b-1),find_max(1,0,n-1,a-1,b-1))