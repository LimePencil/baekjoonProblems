import sys

def mex(p):
    for i in range(len(p)):
        if i!=p[i]:
            return i
    return len(p)

def DFS_single(node):
    global grundy
    if grundy[node][node]!=-1:
        return grundy[node][node]
    s=set()
    for next_node in graph[node]:
        s.add(DFS_single(next_node))
    x=mex(sorted(s))
    grundy[node][node]=x
    return x

def DFS_double(node_1,node_2):
    global grundy
    if grundy[node_1][node_2]!=-1:
        return grundy[node_1][node_2]
    s=set()
    for next_node in graph[node_1]:
        s.add(DFS_double(node_2,next_node))
    for next_node in graph[node_2]:
        s.add(DFS_double(node_1,next_node))
    x=mex(sorted(s))
    grundy[node_1][node_2]=x
    grundy[node_2][node_1]=x
    return x

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000)
n,m=list(map(int,input().split()))
graph=[set() for _ in range(n)]
grundy=[[-1]*n for _ in range(n)]
for i in range(m):
    a,b=list(map(int,input().split()))
    graph[a-1].add(b-1)
for i in range(n):
    graph[i]=list(graph[i])
for i in range(n):
    DFS_single(i)
# for i in range(n):
#     print(grundy[i])
for i in range(n):
    for j in range(n):
        DFS_double(i,j)

# for i in range(n):
#     print(grundy[i])
mal=[[]for _ in range(n)]
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    mal[y-1].append(x-1)
x=0
for i in range(n):
    if len(mal[i])==1:
        x^=grundy[mal[i][0]][mal[i][0]]
    elif len(mal[i])==2:
        x^=grundy[mal[i][0]][mal[i][1]]
print("Young" if x else "Cheol")