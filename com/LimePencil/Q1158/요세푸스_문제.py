# 세그트리 사용

import sys
import math

def init(node, start, end):
    if start == end:
        tree[node] = 1
    else:
        init(node*2, start, (start+end)//2)
        init(node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def find_kth(node, start, end, idx):
    if start == end:
        return start
    if tree[2*node]>= idx:
        return find_kth(2*node,start,(start+end)//2,idx)
    else:
        return find_kth(2*node+1,(start+end)//2+1,end,idx-tree[2*node])

def change_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    if start== end:
        tree[node] = value
        return
    change_tree(2*node,start,(start+end)//2,index,value)
    change_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree[node] = tree[2*node] + tree[2*node+1] 

input = sys.stdin.readline
n,k = map(int,input().split(" "))
tree = [0]*2**(math.ceil(math.log2(n))+1)
init(1,0,n-1)
ans=[]
curr=0
for j in range(n):
    curr+=k-1
    curr%=(n-j)
    i=find_kth(1,0,n-1,curr+1)
    change_tree(1,0,n-1,i,0)
    ans.append(i+1)
print("<"+", ".join(map(str,ans))+">")