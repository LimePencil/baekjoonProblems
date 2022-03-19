import sys
import math

def init(node, start, end):
    if start == end:
        tree[node] = (arr[start],start)
    else:
        init(node*2, start, (start+end)//2)
        init(node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])

def find_min(node, start, end, left,right):
    if left>end or right<start:
        return float('inf')
    if left<=start and end<=right:
        return tree[node]
    return min(find_min(2*node,start,(start+end)//2,left,right), find_min(2*node+1,(start+end)//2+1,end,left,right))

def change_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    if start== end:
        tree[node] = (value,start)
        return
    change_tree(2*node,start,(start+end)//2,index,value)
    change_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree[node] = min(tree[2*node], tree[2*node+1]) 


input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split(" ")))
tree_depth = 2**(math.ceil(math.log2(n))+1)
m = int(input())
tree = [0]*tree_depth
init(1,0,n-1)
for _ in range(m):
    l = list(map(int,input().split(" ")))
    if l[0] ==1:
        a,b,c = l
        change_tree(1,0,n-1,b-1,c)
    else:
        print(find_min(1,0,n-1,0,n-1)[1]+1)