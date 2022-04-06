a=[int(input()) for _ in range(7)]
m=float('inf')
s=0
for c in a:
    if c%2==1:
        m=min(m,c)
        s+=c
if m==float('inf'):
    print(-1)
else:
    print(s)
    print(m)