import sys

def union(p,a,b):
    a = find(p,a)
    b = find(p,b)
    if a< b:
        p[b] = a
    else:
        p[a] = b
def find(p,x):
    if p[x] != x:
        return find(p,p[x])
    return p[x]


input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n =int(input())
    x=[]
    y=[]
    r=[]
    for _ in range(n):
        a,b,c=list(map(int,input().split()))
        x.append(a)
        y.append(b)
        r.append(c)
    ids=list(range(n))
    for i in range(n):
        for j in range(i):
            x1,y1,r1=x[i],y[i],r[i]
            x2,y2,r2=x[j],y[j],r[j]
            if (x1-x2)**2+(y1-y2)**2<=(r1+r2)**2:
                union(ids,i,j)
    cnt=0
    for i in range(n):
        if ids[i] == i:
            cnt +=1
    print(cnt)