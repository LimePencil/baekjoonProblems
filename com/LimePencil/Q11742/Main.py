import sys

def dp(node):
    global visited,nodes
    for e in node:
        if not visited[e]:
            visited[e] = True
            dp(nodes[e])


n, m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
sys.setrecursionlimit(10**4)
nodes = [[] for _ in range(n + 1)]
visited = [False]*(n+1)
count = 0
for i in range(m):
    a, b = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    nodes[b].append(a)
    nodes[a].append(b)
for k, node in enumerate(nodes):
    if not visited[k] and k!=0:
        dp(node)
        count +=1
print(count)

