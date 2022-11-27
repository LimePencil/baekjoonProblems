a,b,c=map(int,input().split())
x,y,z=map(int,input().split())

d_a=min(x,a)
d_b=min(y,b)
d_c=min(z,c)
ans=0
while d_a>0 or d_b>0 or d_c>0:
    d_a=min(x,a)
    d_b=min(y,b)
    d_c=min(z,c)
    ans+=d_a+d_b+d_c
    x-=d_a
    y-=d_b
    z-=d_c
    a-=d_a
    b-=d_b
    c-=d_c
    y+=x//3
    x%=3
    z+=y//3
    y%=3
    x+=z//3
    z%=3
print(ans)