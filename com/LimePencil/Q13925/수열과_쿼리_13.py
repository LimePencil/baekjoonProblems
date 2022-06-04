import sys
import math

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        init(node*2, start, (start+end)//2)
        init(node*2+1, (start+end)//2+1, end)
        tree[node] = (tree[node*2] + tree[node*2+1])% MOD

def lazy_update(node,start,end):
    if lazy[0][node] !=1 or lazy[1][node]!=0:
        tree[node] = (tree[node]*lazy[0][node]+(end-start+1)*lazy[1][node])%MOD
        if start!=end:
            lazy[0][node*2] = (lazy[0][node*2]*lazy[0][node])%MOD
            lazy[0][node*2+1] = (lazy[0][node*2+1]*lazy[0][node])%MOD
            lazy[1][node*2] =(lazy[1][node*2]*lazy[0][node]+lazy[1][node])%MOD
            lazy[1][node*2+1] = (lazy[1][node*2+1]*lazy[0][node]+lazy[1][node])%MOD
    lazy[0][node] =1
    lazy[1][node] =0

def lazy_range(node, start,end,left,right,multiply,add):
    lazy_update(node,start,end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        lazy[0][node]*=multiply
        lazy[1][node]*=multiply
        lazy[0][node]%=MOD
        lazy[1][node]%=MOD
        lazy[1][node]+=add
        lazy[1][node]%=MOD
        lazy_update(node,start,end)
        return
    lazy_range(node*2,start,(start+end)//2,left,right,multiply,add)
    lazy_range(node*2+1,(start+end)//2+1,end,left,right,multiply,add)
    tree[node] = (tree[node*2] + tree[node*2+1])% MOD

def find_sum(node,start,end,left,right):
    lazy_update(node,start,end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return (find_sum(node*2,start,(start+end)//2,left,right)+find_sum(node*2+1,(start+end)//2+1,end,left,right))% MOD

input = sys.stdin.readline
n=int(input())
MOD=1000000007
arr = list(map(int,input().split()))
m=int(input())
tree_depth = 2**(math.ceil(math.log2(n))+1)
tree = [0]*tree_depth
lazy = []
lazy.append([1]*tree_depth)
lazy.append([0]*tree_depth)
init(1,0,n-1)
for _ in range(m):
    l = list(map(int,input().split()))
    if l[0] == 4:
        a,b,c=l
        print(find_sum(1,0,n-1,b-1,c-1))
    else:
        a,b,c,d=l
        if a==1:
            lazy_range(1,0,n-1,b-1,c-1,1,d)
        elif a==2:
            lazy_range(1,0,n-1,b-1,c-1,d,0)
        else:
            lazy_range(1,0,n-1,b-1,c-1,0,d)