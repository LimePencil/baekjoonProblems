import sys

def mex(p):
    for i in range(len(p)):
        if i!=p[i]:
            return i
    return len(p)

def DFS(node,graph,first):
    global grundy
    if not first and grundy[node]!=-1:
        return grundy[node]
    s=set()
    for next_node in graph[node]:
        s.add(DFS(next_node,graph,False))
    x=mex(sorted(s))
    grundy[node]=x
    return x

def calc():
    global grundy
    n,m=list(map(int,input().split()))
    graph=[[] for _ in range(n)]
    grundy=[-1]*n
    first=[True]*n
    for i in range(m):
        a,b=list(map(int,input().split()))
        graph[a-1].append(b-1)
        first[b-1]=False
    for i in range(n):
        if first[i]:
            first[i]=0
            DFS(i,graph,True)
    return grundy[:]


input = lambda: sys.stdin.readline().rstrip()

grundy=[]
grundy_1=calc()
grundy_2=calc()
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    print('W' if grundy_1[x-1]^grundy_2[y-1] else 'P')