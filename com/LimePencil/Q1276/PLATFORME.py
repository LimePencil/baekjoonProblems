import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
pillars=[]
for _ in range(n):
    y,x1,x2=list(map(int,input().split()))
    pillars.append((y,x1,x2))
pillars.sort(key=lambda x:(-x[0],x[1],x[2]))
ans=0
for i in range(n):
    y,x1,x2=pillars[i]
    closest_to_x1=0
    closest_to_x2=0
    for j in range(i+1,n):
        if closest_to_x1!=0 and closest_to_x2!=0:
            break
        y_other,x1_other,x2_other=pillars[j]
        if x1_other<=x1<x2_other and closest_to_x1==0:
            closest_to_x1=y_other
        if x1_other<x2<=x2_other and closest_to_x2==0:
            closest_to_x2=y_other
    ans+=y-closest_to_x1+y-closest_to_x2
print(ans)