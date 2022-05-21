import sys

input = sys.stdin.readline
a,b,c,x,y = list(map(int,input().split()))
ans=0
if c*2<a+b:
    half_chicken=min(x,y)
    ans+=half_chicken*c*2
    x-=half_chicken
    y-=half_chicken

if x>0 and c*2<a:
    ans+=x*c*2
    y-=x
    x=0

if y>0 and c*2<b:
    ans+=y*c*2
    x-=y
    y=0

if x>0:
    ans+=x*a

if y>0:
    ans+=y*b

print(ans)