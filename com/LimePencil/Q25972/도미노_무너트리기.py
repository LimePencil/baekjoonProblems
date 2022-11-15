import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
domino=[list(map(int,input().split())) for _ in range(n)]
domino.sort()
cnt=0
for i in range(n):
    if i==0 or domino[i-1][0]+domino[i-1][1]<domino[i][0]:
        cnt+=1
print(cnt)