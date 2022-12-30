import sys

input = lambda: sys.stdin.readline().rstrip()
a,b = list(map(int,input().split()))
n,m = list(map(int,input().split()))
land=[[None]*(b+1) for _ in range(a+1)]
robots=[None]
dir={"N":0,"E":1,"S":2,"W":3}
for i in range(1,n+1):
    x,y,d=input().split()
    x=int(x)
    y=int(y)
    robots.append([x,y,dir[d]])
    land[x][y]=i
dir=[(0,1),(1,0),(0,-1),(-1,0)]
for _ in range(m):
    r,d,p=input().split()
    r=int(r)
    p=int(p)
    
    for _ in range(p):
        if d=="F":
            if not (0<dir[robots[r][2]][0]+robots[r][0]<=a and 0<dir[robots[r][2]][1]+robots[r][1]<=b):
                print(f"Robot {r} crashes into the wall")
                exit()
            elif land[dir[robots[r][2]][0]+robots[r][0]][dir[robots[r][2]][1]+robots[r][1]]!=None:
                print(f"Robot {r} crashes into robot {land[dir[robots[r][2]][0]+robots[r][0]][dir[robots[r][2]][1]+robots[r][1]]}")
                exit()
            else:
                land[robots[r][0]][robots[r][1]]=None
                land[dir[robots[r][2]][0]+robots[r][0]][dir[robots[r][2]][1]+robots[r][1]]=r
                robots[r][0]+=dir[robots[r][2]][0]
                robots[r][1]+=dir[robots[r][2]][1]
        elif d=="L":
            robots[r][2]-=1
            robots[r][2]%=4
        else:
            robots[r][2]+=1
            robots[r][2]%=4
else:
    print("OK")