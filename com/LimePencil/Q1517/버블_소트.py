# import sys
# import math

# def find_sum(node, start, end, left,right):
#     if left>end or right<start:
#         return 0
#     if left<=start and end<=right:
#         return tree[node]
#     return find_sum(2*node,start,(start+end)//2,left,right) + find_sum(2*node+1,(start+end)//2+1,end,left,right)

# def change_tree(node, start, end, index):
#     if index<start or index>end:
#         return
#     if start== end:
#         tree[node] =1
#         return
#     change_tree(2*node,start,(start+end)//2,index)
#     change_tree(2*node+1,(start+end)//2+1,end,index)
#     tree[node] = tree[2*node] + tree[2*node+1] 


# input = sys.stdin.readline
# n= int(input())
# arr = list(map(int,input().split(" ")))
# arr2 = {v:i for i,v in enumerate(sorted(arr))}
# tree_depth = 2**(math.ceil(math.log2(n))+1)
# tree = [0]*tree_depth
# ans = 0
# for v in arr:
#     i = arr2[v]
#     ans+=find_sum(1,0,n-1,i+1,n-1)
#     change_tree(1,0,n-1,i)
# print(ans)

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
n = int(input())
arr = list(map(int,input().split()))
temp=sorted(arr)
d={temp[i]:i+1 for i in range(n)}
for i in range(n):
    arr[i]=d[arr[i]]
tree = [0]*(n+1)
ans=0
for i in range(n):
    ans+=query(n)-query(arr[i])
    update(arr[i],1)
print(ans)