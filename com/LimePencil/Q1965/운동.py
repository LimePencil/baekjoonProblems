import sys

def Floyd_Warshall():
    return
input = sys.stdin.readline
v,e = list(map(int,input().split(" ")))
f = [[float('inf') for _ in range(v+1)]for _ in range(v+1)]
for _ in range(e):
    a,b,c = list(map(int,input().split(" ")))
    f[a][b] = c
for k in range(v+1):
    for i in range(v+1):
        for j in range(v+1):
            f[i][j] = min(f[i][j],f[i][k]+f[k][j])
cycle = float('inf')
for i in range(v+1):
    for j in range(v+1):
        if i ==j:
            continue
        cycle = min(cycle,f[i][j]+f[j][i])
if cycle == float('inf'):
    print(-1)
else:
    print(cycle)