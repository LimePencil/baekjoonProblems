import sys



n, k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
items = []
table = [[0 for i in range(k+1)] for j in range(n+1)]
for i in range(n):
    items.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))

for i in range(1,n+1):
    for j in range(k+1):
        w = items[i-1][0]
        v = items[i-1][1]
        if j<w:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(v+ table[i-1][j-w],table[i-1][j])
print(table[n][k])

