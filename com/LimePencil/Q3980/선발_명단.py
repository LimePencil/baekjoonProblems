import sys

input = lambda: sys.stdin.readline().rstrip()

def dfs(curr,sum):
    global ans
    if curr==11:
        ans=max(sum,ans)
    for i in range(11):
        if not visited[i] and stat[curr][i]!=0:
            visited[i]=True
            dfs(curr+1,sum+stat[curr][i])
            visited[i]=False
    

t = int(input())
for _ in range(t):
    stat=[]
    visited=[False]*11
    ans=0
    for i in range(11):
        arr=list(map(int,input().split()))
        stat.append(arr)
    dfs(0,0)
    print(ans)