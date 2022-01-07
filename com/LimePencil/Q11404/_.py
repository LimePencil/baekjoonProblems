import sys


n = int(sys.stdin.readline().rstrip("\n"))
d = [[float("inf") for _ in range(n)] for _ in range(n)]
k = int(sys.stdin.readline().rstrip("\n"))


for i in range(k):
    s, e, v = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    d[s-1][e-1] = min(v,d[s-1][e-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                d[i][j] = 0
            else:
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
for i in range(n):
    for j in range(n):
        if d[i][j] == float('inf'):
            d[i][j] = 0
for o in range(n):
    print(*d[o])