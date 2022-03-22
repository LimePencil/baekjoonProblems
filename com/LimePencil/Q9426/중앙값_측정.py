import sys
import math

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
        tree[node] += value
        return
    change_tree(2*node,start,(start+end)//2,index,value)
    change_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree[node] = tree[2*node] + tree[2*node+1] 

N = 65536
input = sys.stdin.readline
n,k = list(map(int,input().split(" ")))
arr = []
for _ in range(n):
    arr.append(int(input()))
tree_depth = 2**(math.ceil(math.log2(N))+1)
tree = [0]*tree_depth
ans = 0
for i in range(k-1):
    change_tree(1,0,N-1,arr[i],1)
for i in range(k-1,n):
    change_tree(1,0,N-1,arr[i],1)
    ans += find_kth(1,0,N-1,(k+1)//2)
    change_tree(1,0,N-1,arr[i-k+1],-1)
print(ans)