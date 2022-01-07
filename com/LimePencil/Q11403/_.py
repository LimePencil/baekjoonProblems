import sys

d = []
n = int(sys.stdin.readline().rstrip("\n"))
for i in range(n):
    d.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] == 1 and d[k][j] ==1:
                d[i][j] =1
for o in range(n):
    print(*d[o])