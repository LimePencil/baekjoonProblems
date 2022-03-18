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
n,m = list(map(int,input().split(" ")))
arr = []
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [0]*tree_depth
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    if a ==1:
        change_tree(1,0,n-1,b-1,c)
    else:
        if b> c:
            b,c = c,b
        print(find_sum(1,0,n-1,b-1,c-1))