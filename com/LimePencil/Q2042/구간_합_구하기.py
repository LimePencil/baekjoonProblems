# SEGMENT TREE
# 
# 
# import sys
# import math

# def init(node, start, end):
#     if start == end:
#         tree[node] = arr[start]
#     else:
#         init(node*2, start, (start+end)//2)
#         init(node*2+1, (start+end)//2+1, end)
#         tree[node] = tree[node*2] + tree[node*2+1]

# def find_sum(node, start, end, left,right):
#     if left>end or right<start:
#         return 0
#     if left<=start and end<=right:
#         return tree[node]
#     return find_sum(2*node,start,(start+end)//2,left,right) + find_sum(2*node+1,(start+end)//2+1,end,left,right)

# def change_tree(node, start, end, index,value):
#     if index<start or index>end:
#         return
#     if start== end:
#         arr[index] = value
#         tree[node] = value
#         return
#     change_tree(2*node,start,(start+end)//2,index,value)
#     change_tree(2*node+1,(start+end)//2+1,end,index,value)
#     tree[node] = tree[2*node] + tree[2*node+1] 


# input = sys.stdin.readline
# n,m,k = list(map(int,input().split(" ")))
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
# tree_depth = 2**(math.ceil(math.log2(n))+1)
# tree = [0]*tree_depth
# init(1,0,n-1)
# for _ in range(m+k):
#     a,b,c = list(map(int,input().split(" ")))
#     if a ==1:
#         change_tree(1,0,n-1,b-1,c)
#     else:
#         print(find_sum(1,0,n-1,b-1,c-1))


# FENWICK TREE

import sys

def update(idx, val):
    while idx <= n:
        tree[idx]+= val
        idx+= (idx&-idx)

def query(idx):
    ans =0
    while idx>0:
        ans+= tree[idx]
        idx-=(idx&-idx)
    return ans

input = sys.stdin.readline
n,m,k = list(map(int,input().split(" ")))
arr = [0]
tree = [0]*(n+1)
for i in range(1,n+1):
    e = int(input())
    update(i,e)
    arr.append(e)

for _ in range(m+k):
    a,b,c = list(map(int,input().split(" ")))
    if a ==1:
       update(b,c-arr[b]) 
       arr[b] = c
    else:
        print(query(c)-query(b-1))