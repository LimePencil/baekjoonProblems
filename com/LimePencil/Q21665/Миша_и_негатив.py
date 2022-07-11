import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
ori=[list(input().rstrip()) for _ in range(n)]
input().rstrip()
new=[list(input().rstrip()) for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(m):
        if ori[i][j]==new[i][j]:
            cnt+=1
print(cnt)