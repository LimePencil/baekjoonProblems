x,y=map(int,input().split())
r=int(input())
d=[(1,1),(1,-1),(-1,-1),(-1,1)]
for i in range(4):
    print(x+r*d[i][0],y+r*d[i][1])