import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
coins=[list(map(int,list(input()))) for _ in range(n)]
cnt=0
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if coins[i][j]==1:
            cnt+=1
            for k in range(i+1):
                for l in range(j+1):
                    coins[k][l]^=1
print(cnt)