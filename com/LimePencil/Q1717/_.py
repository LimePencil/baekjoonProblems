import sys

def union(a,b):
    a = find(a)
    b = find(b)
    if a< b:
        p[b] = a
    else:
        p[a] = b
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
        return p[x]
    return p[x]
sys.setrecursionlimit(10**8)
n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
p = list(range(n+1))
for _ in range(m):
    o,a,b = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    if o == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")