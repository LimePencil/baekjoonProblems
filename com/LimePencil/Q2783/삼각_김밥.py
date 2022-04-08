x,y=map(int,input().split())
m=x/y*1000
for _ in range(int(input())):
    a,b=map(int,input().split())
    m=min(m,a/b*1000)
print(m)