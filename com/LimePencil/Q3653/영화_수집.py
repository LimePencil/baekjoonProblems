import sys
import math

def find_sum(node, start, end, left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[node]
    return find_sum(2*node,start,(start+end)//2,left,right) + find_sum(2*node+1,(start+end)//2+1,end,left,right)

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
t= int(input())
for _ in range(t):
    n,m = list(map(int,input().split(" ")))
    arr= list(map(int,input().split(" ")))
    idx = [0]*(n)
    tree = [0]*2**(math.ceil(math.log2(n+m))+1)
    for k in range(m,m+n):
        change_tree(1,0,n+m-1,k,1)
        idx[k-m]=k
    ans = []
    curr_i = m-1
    for i in range(m):
        ans.append(str(find_sum(1,0,n+m-1,0,idx[arr[i]-1]-1)))
        change_tree(1,0,n+m-1,idx[arr[i]-1],0)
        curr_i-=1
        idx[arr[i]-1] = curr_i
        change_tree(1,0,n+m-1,curr_i,1)
    print(*ans)