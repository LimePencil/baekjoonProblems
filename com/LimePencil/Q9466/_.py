import sys

def dfs(v):
    global ans
    stack = [v]
    tr.append(v)
    w = graph[v]
    visit[v] = True
    if visit[w]:
        a = 0
        try:
            a = tr.index(w)
        except:
            a = -1
        if a != -1:
            ans += tr[a:]
    else:
        dfs(w)
sys.setrecursionlimit(10**6)
t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t): 
    n = int(sys.stdin.readline().rstrip("\n"))
    ans = []
    graph = [0]*(n+1)
    arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    for k,c in enumerate(arr):
        graph[k+1] =c
    visit = [False for _ in range(n+1)]
    for i in range(1,n+1):
        if not visit[i]:
            tr = []
            dfs(i)
    print(n-len(ans))
