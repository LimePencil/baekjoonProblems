import sys

def dfs(x,y,visited,l):
    global max_len
    th=(ord(table[x][y])-65)
    if visited & (1<<th):
        return
    visited+=1<<th
    max_len=max(max_len,l+1)
        
    for i in range(4):
        nx=x+dir[i][0]
        ny=y+dir[i][1]
        if 0<=nx<n and 0<=ny<m:
            dfs(nx,ny,visited,l+1)

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
table=[input() for _ in range(n)]
dir=[(1,0),(-1,0),(0,1),(0,-1)]
max_len=0
dfs(0,0,0,0)
print(max_len)