a,b,c,d=map(int,input().split())
x=c*60+d-a*60-b
if x<0:
    x+=1440
print(x,x//30)