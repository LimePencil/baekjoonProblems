import sys

input = lambda: sys.stdin.readline().rstrip()
table=[[0]*19 for _ in range(19)]
n = int(input())
omok=False
for i in range(n):
    x,y=list(map(int,input().split()))
    x-=1
    y-=1
    table[x][y]=1 if i%2==0 else 2
    dir=[(1,0),(1,1),(1,-1),(0,1)]
    for dx,dy in dir:
        length=1
        for j in range(1,5):
            nx=x+dx*j
            ny=y+dy*j
            if 0<=nx<19 and 0<=ny<19 and table[nx][ny]==table[x][y]:
                length+=1
                continue
            else:
                break
        for j in range(-1,-5,-1):
            nx=x+dx*j
            ny=y+dy*j
            if 0<=nx<19 and 0<=ny<19 and table[nx][ny]==table[x][y]:
                length+=1
                continue
            else:
                break
        if length==5:
            omok=True
            break
    if omok:
        print(i+1)
        break
if not omok:
    print(-1)

