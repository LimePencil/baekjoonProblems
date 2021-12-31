import sys

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
table = [0] + list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
for i in range(1,n+1):
        table[i] += table[i-1]
for _ in range(m):
    x1,x2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    print(table[x2] - table[x1-1])