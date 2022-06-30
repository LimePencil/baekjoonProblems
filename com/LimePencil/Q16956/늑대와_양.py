import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
map=[]
loc=[]
for i in range(n):
    s=input().rstrip().replace(".","D")
    for j in range(m):
        if s[j]=="W":
            loc.append((i,j))
    map.append(s)
    
dir=[(0,1),(0,-1),(1,0),(-1,0)]
ans=1
for x,y in loc:
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<m and map[nx][ny]=="S":
            ans=0
            break
    if ans==0:
        break
print(ans)
if ans!=0:
    for i in range(n):
        print(map[i])