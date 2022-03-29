x,y,d,t = list(map(int,input().split()))
c=(x**2+y**2)**0.5
if c>=d:
    a=c//d
    print(min(c-d*a+a*t,(a+1)*t,c))
else:
    print(min(t*2,c,t+d-c))