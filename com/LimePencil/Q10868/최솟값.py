import sys
import math

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(node*2, start, (start+end)//2)
        init(node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node*2],tree[node*2+1])

def find_min(node, start, end, left,right):
    if left>end or right<start:
        return float('inf')
    if left<=start and end<=right:
        return tree[node]
    return min(find_min(2*node,start,(start+end)//2,left,right), find_min(2*node+1,(start+end)//2+1,end,left,right))

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
arr = [int(input()) for _ in range(n)]
tree = [0]*2**(math.ceil(math.log2(n))+1)
init(1,0,n-1)
for _ in range(m):
    a,b = list(map(int,input().split(" ")))
    print(find_min(1,0,n-1,a-1,b-1))