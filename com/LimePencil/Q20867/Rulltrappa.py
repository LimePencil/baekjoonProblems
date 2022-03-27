m,s,g=map(int,input().split())
a,b=map(float,input().split())
l,r=map(int,input().split())
c=l/a+m/g
d=r/b+m/s
print("latmask" if c>d else "friskus")