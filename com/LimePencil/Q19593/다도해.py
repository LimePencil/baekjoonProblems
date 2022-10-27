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
    n,s,a,b=list(map(int,input().split()))
    p=list(range(n))
    for i in range(1,n**2+1):
        if i==1:
            e=s%(n**2)
            x=e//n
            y=e%n
        else:
            e=(e*a+b)%(n**2)
            x=e//n
            y=e%n
        union(p,x,y)
        cnt=0
        for j in range(n):
            if p[j] == j:
                cnt +=1
        if cnt==1:
            print(i)
            break
    else:
        print(0)
