import sys

def dfs(left,right,graph):
    stack=[(1,0)]
    idx=1
    visited=[False]*(n+1)
    while stack:
        i,k=stack.pop()
        visited[i]=True
        if left[i]==0:
            left[i]=idx
        if k==len(graph[i]):
            right[i]=idx
        else:   
            stack.append((i,k+1))
            if not visited[graph[i][k]]: 
                idx+=1
                stack.append((graph[i][k],0))
def update(idx, val1,val2):
    while idx <= n:
        tree_one[idx]^= val1
        tree_two[idx]^=val2
        idx+= (idx&-idx)

def range_update(left,right,val):
    update(left,val,((-left+1)%2)*val)
    update(right+1,val,((right)%2)*val)

def query(idx):
    val1=0
    val2=0
    f=idx
    while idx>0:
        val1^= tree_one[idx]
        val2^= tree_two[idx]
        idx-=(idx&-idx)
    return (val1*(f%2))^val2

input = sys.stdin.readline
n,m = list(map(int,input().split()))
table=[[]for _ in range(n+1)]
tree_one = [0]*(n+1)
tree_two = [0]*(n+1)
left=[0]*(n+1)
right=[0]*(n+1)
for _ in range(n-1):
    a,b=list(map(int,input().split()))
    table[a].append(b)
    table[b].append(a) 
dfs(left,right,table)
weight=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    range_update(left[i],left[i],weight[i])
for _ in range(m):
    l = list(map(int,input().split()))
    if l[0] ==2:
       range_update(left[l[1]],right[l[1]],l[2]) 
    else:
        a=query(left[l[1]]-1)
        b=query(right[l[1]])
        print(a^b)