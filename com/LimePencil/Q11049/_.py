import sys

n = int(sys.stdin.readline().rstrip("\n"))
arr =[]
mem = [[0 for _ in range(n)]for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
for i in range(1,n):
    for j in range(n-i):
        if i ==1:
            mem[j][j+i] = arr[j][0]*arr[j][1]*arr[j+i][1]
            continue
        mem[j][j+i] = float('inf')
        for k in range(j,j+i):
            mem[j][j+i] = min(mem[j][j+i], mem[j][k] + mem[k+1][j+i]+arr[j][0]*arr[k][1]*arr[j+i][1])
print(mem[0][n-1])
