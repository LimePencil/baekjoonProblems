import sys

input = lambda: sys.stdin.readline().rstrip()
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if a[i]==b[i]==c[i]:
        continue
    else:
        if a[i]==b[i] and b[i]!=c[i]:
            x=c.index(a[i])
            c.pop(x)
            c.insert(i,a[i])
        elif a[i]==c[i] and b[i]!=c[i]:
            x=b.index(a[i])
            b.pop(x)
            b.insert(i,a[i])
        else:
            x=a.index(b[i])
            a.pop(x)
            a.insert(i,b[i])
print(*a)