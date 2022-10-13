import sys

input = lambda: sys.stdin.readline().rstrip()
r,c,n = list(map(int,input().split()))
grid=[list(input()) for _ in range(r)]
diff_grid=[["O"]*c for _ in range(r)]
if n%2==0:
    for i in range(r):
        print(*diff_grid[i],sep="")
elif n%4==3:
    dir=[(0,0),(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(r):
        for j in range(c):
            if grid[i][j]=="O":
                for di,dj in dir:
                    ni=di+i
                    nj=dj+j
                    if 0<=ni<r and 0<=nj<c:
                        diff_grid[ni][nj]="."
    for i in range(r):
        print(*diff_grid[i],sep="")
elif n!=1 and n%4==1:
    dir=[(0,0),(1,0),(0,1),(-1,0),(0,-1)]
    diff_grid=[["."]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j]=="O":
                for di,dj in dir:
                    ni=di+i
                    nj=dj+j
                    if 0<=ni<r and 0<=nj<c:
                        diff_grid[ni][nj]="O"
    grid=[["O"]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if diff_grid[i][j]==".":
                for di,dj in dir:
                    ni=di+i
                    nj=dj+j
                    if 0<=ni<r and 0<=nj<c:
                        grid[ni][nj]="."
    for i in range(r):
        print(*grid[i],sep="")

else:
    for i in range(r):
        print(*grid[i],sep="")