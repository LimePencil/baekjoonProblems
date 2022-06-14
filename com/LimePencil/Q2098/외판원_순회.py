import sys

def DFS(node,path):
    if path == (1<<n)-1:
        if ways[node][0] !=0:
            return ways[node][0]
        else:
            return 10**9
    if cost[node][path]!=0:
        return cost[node][path]
    limit=10**9
    for next_node in range(0,n):
        if ways[node][next_node] ==0 or path&(1<<next_node)!=0:
            continue
        limit = min(limit,ways[node][next_node]+DFS(next_node,path|1<<next_node))
    cost[node][path]=limit
    return cost[node][path]

input = sys.stdin.readline
n = int(input())
ways=[list(map(int,input().split())) for _ in range(n)]
cost=[[0]*(1<<n) for _ in range(n)]
print(DFS(0,1))