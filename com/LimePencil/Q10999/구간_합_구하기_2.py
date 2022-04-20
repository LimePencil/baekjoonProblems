# import sys
# import math

# def init(node, start, end):
#     if start == end:
#         tree[node] = arr[start]
#     else:
#         init(node*2, start, (start+end)//2)
#         init(node*2+1, (start+end)//2+1, end)
#         tree[node] = tree[node*2] + tree[node*2+1]

# def lazy_update(node,start,end):
#     if lazy[node] !=0:
#         tree[node] += (end-start+1)*lazy[node]
#         if start!=end:
#             lazy[node*2] += lazy[node]
#             lazy[node*2+1] += lazy[node]
#         lazy[node] = 0


# def lazy_range(node, start,end,left,right,value):
#     lazy_update(node,start,end)
#     if left > end or right < start:
#         return
#     if left <= start and end <= right:
#         tree[node] += (end-start+1)*value
#         if start != end:
#             lazy[node*2] += value
#             lazy[node*2+1] += value
#         return
#     lazy_range(node*2,start,(start+end)//2,left,right,value)
#     lazy_range(node*2+1,(start+end)//2+1,end,left,right,value)
#     tree[node] = tree[node*2] + tree[node*2+1]

# def find_sum(node,start,end,left,right):
#     lazy_update(node,start,end)
#     if left > end or right < start:
#         return 0
#     if left <= start and end <= right:
#         return tree[node]
#     return find_sum(node*2,start,(start+end)//2,left,right) +find_sum(node*2+1,(start+end)//2+1,end,left,right)

# input = sys.stdin.readline
# n,m,k = list(map(int,input().split(" ")))
# arr = [int(input()) for _ in range(n)]
# tree_depth = 2**(math.ceil(math.log2(n))+1)
# tree = [0]*tree_depth
# lazy = [0]*tree_depth
# init(1,0,n-1)
# for _ in range(m+k):
#     l = list(map(int,input().split(" ")))
#     if l[0] == 1:
#         lazy_range(1,0,n-1,l[1]-1,l[2]-1,l[3])
#     else:
#         print(find_sum(1,0,n-1,l[1]-1,l[2]-1))

# fenwick tree
import sys
def update(idx, val1,val2):
    while idx <= n:
        tree_one[idx]+= val1
        tree_two[idx]+=val2
        idx+= (idx&-idx)

def range_update(left,right,val):
    update(left,val,(-left+1)*val)
    update(right+1,-val,right*val)

def query(idx):
    val1=0
    val2=0
    f=idx
    while idx>0:
        val1+= tree_one[idx]
        val2+= tree_two[idx]
        idx-=(idx&-idx)
    return val1*f+val2

input = sys.stdin.readline
n,m,k = list(map(int,input().split()))
tree_one = [0]*(n+1)
tree_two = [0]*(n+1)
for i in range(1,n+1):
    x=int(input())
    range_update(i,i,x)
for _ in range(m+k):
    l = list(map(int,input().split(" ")))
    if l[0] ==1:
       range_update(l[1],l[2],l[3]) 
    else:
        print(query(l[2])-query(l[1]-1))