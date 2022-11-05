import sys

input = lambda: sys.stdin.readline().rstrip()
l,n,f,b= list(map(int,input().split()))
stops=[]
for _ in range(n):
    x,c=list(map(int,input().split()))
    stops.append((x,c))
stops.sort(key=lambda a: (-a[1],a[0]))
viable_stops=[stops[0]]
for i in range(1,n):
    if viable_stops[-1][0]<stops[i][0]:
        viable_stops.append(stops[i])
cow_pos=0
tastiness=0
for x,c in viable_stops:
    tastiness+=(x-cow_pos)*(f-b)*c
    cow_pos=x
print(tastiness)
