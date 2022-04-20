import sys

def dfs(left,right,graph,start,depth):
    stack=[(start,0,1)]
    idx=1
    visited=[False]*(n+1)
    while stack:
        i,k,d=stack.pop()
        
        visited[i]=True
        if left[i]==0:
            left[i]=idx
            depth[i]=d
        if k==len(graph[i]):
            right[i]=idx
        else:   
            stack.append((i,k+1,d))
            if not visited[graph[i][k]]: 
                idx+=1
                stack.append((graph[i][k],0,d+1))
def update(idx, val):
    while idx <= n:
        tree[idx]+= val
        idx+= (idx&-idx)

def query(idx):
    ans =0
    while idx>0:
        ans+= tree[idx]
        idx-=(idx&-idx)
    return ans

input = sys.stdin.readline
n,c = list(map(int,input().split()))
table=[[]for _ in range(n+1)]
tree = [0]*(n+1)
left=[0]*(n+1)
right=[0]*(n+1)
depth=[0]*(n+1)
for _ in range(n-1):
    a,b=list(map(int,input().split()))
    table[a].append(b)
    table[b].append(a)
dfs(left,right,table,c,depth)
for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    if x==1:
        update(left[y],1)
    else:
        print((query(right[y])-query(left[y]-1))*depth[y])