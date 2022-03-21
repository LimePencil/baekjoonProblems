import sys
import math

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]%2
    else:
        init(node*2, start, (start+end)//2)
        init(node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2]+ tree[node*2+1]

def find_odd(node, start, end, left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[node]
    return find_odd(2*node,start,(start+end)//2,left,right)+ find_odd(2*node+1,(start+end)//2+1,end,left,right)

def change_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    if start== end:
        tree[node] = value%2
        return
    change_tree(2*node,start,(start+end)//2,index,value)
    change_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree[node] = tree[2*node]+ tree[2*node+1]


input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split(" ")))
tree_depth = 2**(math.ceil(math.log2(n))+1)
m = int(input())
tree = [0]*tree_depth
init(1,0,n-1)
for _ in range(m):
    a,b,c = list(map(int,input().split(" ")))
    if a ==1:
        change_tree(1,0,n-1,b-1,c)
    elif a ==2:
        print(c-b+1-find_odd(1,0,n-1,b-1,c-1))
    else:
        print(find_odd(1,0,n-1,b-1,c-1))