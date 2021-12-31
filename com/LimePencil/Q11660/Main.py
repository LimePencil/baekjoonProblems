import sys

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
table = []*(n+1)
table.append([0]*(n+1))
for _ in range(n):
    table.append([0] + list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
for i in range(1,n+1):
    for j in range(1,n+1):
        table[i][j] += table[i][j-1] + table[i-1][j] - table[i-1][j-1]
for _ in range(m):
    x1,y1,x2,y2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    print(table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] +table[x1-1][y1-1])