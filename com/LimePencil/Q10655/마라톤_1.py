import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
s=0
dist=[]
for i in range(n-1):
    d=abs(points[i][0]-points[i+1][0])+abs(points[i][1]-points[i+1][1])
    dist.append(d)
    s+=d
diff=0
for i in range(n-2):
    d=abs(points[i][0]-points[i+2][0])+abs(points[i][1]-points[i+2][1])
    diff=max(diff,dist[i]+dist[i+1]-d)
print(s-diff)