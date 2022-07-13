import sys

input = sys.stdin.readline

for _ in range(int(input())):
    ans = 0
    area=[[0]*10000 for _ in range(10000)]
    n=int(input())
    for _ in range(n):
        x,y=list(map(int,input().split()))
        for dx in range(11):
            for dy in range(11):
                nx=x-dx
                ny=y-dy
                if 0<=nx<10000 and 0<=ny<10000:
                    area[nx][ny]+=1
                    ans=max(ans,area[nx][ny])
    print(ans)
    del(area)