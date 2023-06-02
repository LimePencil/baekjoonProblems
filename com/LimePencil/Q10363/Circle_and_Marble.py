import sys

def mex(p):
    for i in range(len(p)):
        if i!=p[i]:
            return i
    return len(p)

def DFS(node):
    global grundy
    s=set()
    for next_node in graph[node]:
        s.add(DFS(next_node))
    x=mex(sorted(s))
    grundy[node]=x
    return x

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
grundy=[]
for t in range(1,int(input())+1):
    n=int(input())
    m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    graph=[[] for _ in range(n)]
    grundy=[0]*n
    x=0
    for idx,node in enumerate(p):
        if idx==0:
            continue
        graph[node-1].append(idx)
    DFS(0)

    for i in range(n):
        if m[i]%2:
            x^=grundy[i]
    print(f"Case #{t}: {'first' if x else 'second'}")