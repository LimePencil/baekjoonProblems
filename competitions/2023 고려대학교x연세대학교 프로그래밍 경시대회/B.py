n=int(input())
arr=sorted(list(map(int,input().split())))
o=float('inf')
e=float('inf')
for i in range(n-1):
    d=arr[i+1]-arr[i]
    if d%2==0:
        e=min(e,d)
    else:
        o=min(o,d)
if o==float('inf'):
    o=-1
elif e==float('inf') and n>2:
    for i in range(n-2):
        d=arr[i+2]-arr[i]
        if d%2==0:
            e=min(e,d)
elif e==float('inf') and n==2:
    e=-1
print(e,o)