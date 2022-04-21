import sys
import math

def dfs(left,right,buhas):
    stack=[(1,0)]
    idx=1
    while stack:
        i,k=stack.pop()
        if left[i]==0:
            left[i]=idx
        if k==len(buhas[i]):
            right[i]=idx
        else:
            idx+=1
            stack.append((i,k+1))
            stack.append((buhas[i][k],0))

def init(node, start, end):
    if start == end:
        tree[node] = 1
    else:
        init(node*2, start, (start+end)//2)
        init(node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def lazy_update(node,start,end):
    if lazy[node] !=0:
        tree[node] = end-start+1 if lazy[node]==1 else 0
        if start!=end:
            lazy[node*2] = lazy[node]
            lazy[node*2+1] = lazy[node]
        lazy[node] = 0


def lazy_range(node, start,end,left,right,value):
    lazy_update(node,start,end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        lazy[node]=value
        lazy_update(node,start,end)
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
buhas=[[]for _ in range(n+1)]
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [0]*tree_depth
lazy = [0]*tree_depth
left=[0]*(n+1)
right=[0]*(n+1)
price=[0]*(n+1)
sawons=list(map(int,input().split()))
m=int(input())
for i in range(1,n):
    buhas[sawons[i]].append(i+1)
dfs(left,right,buhas)
init(1,0,n-1)
for _ in range(m):
    a,b = list(map(int,input().split()))
    if a ==1:
       lazy_range(1,0,n-1,left[b],right[b]-1,1)
    elif a==3:
        print(find_sum(1,0,n-1,left[b],right[b]-1))
    else:
        lazy_range(1,0,n-1,left[b],right[b]-1,-1)