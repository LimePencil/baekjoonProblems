import sys
import math

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(node*2, start, (start+end)//2)
        init(node*2+1, (start+end)//2+1, end)
        tree[node] = (tree[node*2] * tree[node*2+1])

def find_product(node, start, end, left,right):
    if left>end or right<start:
        return 1
    if left<=start and end<=right:
        return tree[node]
    return (find_product(2*node,start,(start+end)//2,left,right) * find_product(2*node+1,(start+end)//2+1,end,left,right))

def change_tree(node, start, end, index,value):
    if index<start or index>end:
        return
    if start== end:
        tree[node] = value
        return
    change_tree(2*node,start,(start+end)//2,index,value)
    change_tree(2*node+1,(start+end)//2+1,end,index,value)
    tree[node] = (tree[2*node] * tree[2*node+1])


input = sys.stdin.readline
while True:
    try:
        n,m = list(map(int,input().split(" ")))
    except:
        break
    arr = list(map(int,input().split(" ")))
    for i in range(n):
        if arr[i] >0:
            arr[i] = 1
        elif arr[i] < 0:
            arr[i] = -1
    tree_depth = 2**(math.ceil(math.log2(n))+1)
    tree = [0]*tree_depth
    init(1,0,n-1)
    for _ in range(m):
        a,b,c = input().rstrip("\n").split(" ")
        b = int(b)
        c = int(c)
        if a =="C":
            if c >0:
                c = 1
            elif c<0:
                c = -1
            change_tree(1,0,n-1,b-1,c)
        else:
            d = find_product(1,0,n-1,b-1,c-1)
            if d >0:
                print("+",end="")
            elif d ==0:
                print("0",end="")
            else:
                print("-",end="")
    print()