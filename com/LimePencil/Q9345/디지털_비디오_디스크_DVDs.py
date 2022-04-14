import sys
import math
def init_min(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
    else:
        init_min(node*2, start, (start+end)//2)
        init_min(node*2+1, (start+end)//2+1, end)
        tree_min[node] = min(tree_min[node*2],tree_min[node*2+1])

def init_max(node, start, end):
    if start == end:
        tree_max[node] = arr[start]
    else:
        init_max(node*2, start, (start+end)//2)
        init_max(node*2+1, (start+end)//2+1, end)
        tree_max[node] = max(tree_max[node*2],tree_max[node*2+1])

def find_min(node, start, end, left,right):
    if left>end or right<start:
        return float('inf')
    if left<=start and end<=right:
        return tree_min[node]
    return min(find_min(2*node,start,(start+end)//2,left,right), find_min(2*node+1,(start+end)//2+1,end,left,right))

def find_max(node, start, end, left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree_max[node]
    return max(find_max(2*node,start,(start+end)//2,left,right), find_max(2*node+1,(start+end)//2+1,end,left,right))

def change_min_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    if start== end:
        arr[index] = value
        tree_min[node] = value
        return
    change_min_tree(2*node,start,(start+end)//2,index,value)
    change_min_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree_min[node] = min(tree_min[2*node],tree_min[2*node+1])

def change_max_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    if start== end:
        arr[index] = value
        tree_max[node] = value
        return
    change_max_tree(2*node,start,(start+end)//2,index,value)
    change_max_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree_max[node] = max(tree_max[2*node],tree_max[2*node+1])

input = sys.stdin.readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    tree_min = [0]*2**(math.ceil(math.log2(n))+1)
    tree_max = [0]*2**(math.ceil(math.log2(n))+1)
    arr=list(range(n))
    init_min(1,0,n-1)
    init_max(1,0,n-1) 
    for _ in range(k):
        q,a,b=map(int,input().split())
        if q==0:
            t1=arr[a]
            t2=arr[b]
            change_max_tree(1,0,n-1,a,t2)
            change_max_tree(1,0,n-1,b,t1)
            change_min_tree(1,0,n-1,a,t2)
            change_min_tree(1,0,n-1,b,t1)
        else:
            if find_min(1,0,n-1,a,b)==a and find_max(1,0,n-1,a,b)==b:
                print("YES")
            else:
                print("NO")